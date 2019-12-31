import random
import itertools

import math
from multiset import Multiset
from scipy.stats import pearsonr
import networkx as nx
import matplotlib.pyplot as plt
import copy
import time

from simulator.gan_metasim import Generator


#Function to get results from the generator network
def get_values_from_generator(j, i, enzyme_size, result):
    offset = i * enzyme_size * 2
    input_value = result[offset + j]
    input_value = floor_or_ceil_value(get_value_from_rage(input_value))
    out_value = result[offset + j + enzyme_size]
    out_value = floor_or_ceil_value(get_value_from_rage(out_value))
    return input_value, out_value

#Function to get result from sigmoid function to metabolic
def get_value_from_rage(OldValue):
    NewMax = len(m_types)
    NewMin = 0
    OldMax = 1
    OldMin = 0
    OldRange = (OldMax - OldMin)
    NewRange = (NewMax - NewMin)
    NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
    return NewValue

#get the value to be "int"
def floor_or_ceil_value(value):
    if(value - math.floor(value) > 0.5):
        return math.ceil(value)
    else:
        return math.floor(value)

class Enzyme: 
    def __init__(self,inp,output):
        self._substrate_def = Multiset(inp)
        self._product_def = Multiset(output)
        self._substrate=Multiset()
    
    def collectall(self, substrate):
        missing = self._substrate_def - self._substrate
        missing &= substrate #Can I complete it with what I have in my "home"
        self._substrate += missing
        substrate.difference_update(missing)

    def isready(self):
        return self._substrate == self._substrate_def
    
    def react(self, substrate):
        if self.isready():
            self._substrate.clear()
            substrate.update(self._product_def)
            return True
        else:
            return False
        
    def __str__(self):
        return "{'inputs':" + str(list(self._substrate_def)) + ", 'outputs':" + str(list(self._product_def)) + "}"
    def __repr__(self):
        return (str(self))  
    def getsubstratedef(self):
        return list(self._substrate_def)
    def getproductdef(self):
        return list(self._product_def)
    

class Species: #improtant note at 25 minute
    def __init__(self,enz,substrate_generator, substrate_size):
        self._enzymes = copy.deepcopy(enz)
        self._substrate_generator = substrate_generator
        self._substrate_size = substrate_size
        self._substrate = Multiset(self._substrate_generator(self._substrate_size))
        self._age=0
        self._reactions=0
    def develop(self,duration):
        for age in range(duration):
            e = random.choice(self._enzymes)
            e.collectall(self._substrate)
            if e.react(self._substrate):
                self._reactions+=1
            self._age+=1
        return self._reactions
    def measure_metabolite_level(self, m):
        return self._substrate[m]
    def getsubstrate(self):
        return self._substrate
    def getenzymes(self):
        return self._ezymes
    def clone(self):
        return copy.deepcopy(self)
    def spawn(self):
        return Species(self._enzymes,self._substrate_generator,self._substrate_size)
    
        
def make_random_sequence_generator(r):
    def generator(count):
        for i in range(count):
            yield random.choice(r)
    return generator

def z(): 
    return 0




#######################################################################
## simulation settings

mtype_count = 200
enzyme_size = 5
enzyme_count = 100
enzymes_per_species = enzyme_count #used to be 80, in recording 24/12/19 38:00
substrate_size = 10000
number_of_samples = 1
number_of_species = 5#1 #100
max_age = 10000

m_types = range(mtype_count) #m_typs is all the metabolics
m_generator = make_random_sequence_generator(m_types)
#todo: call the generator here
enzymes = []
generator_out_layer_size = 2*enzyme_size*enzyme_count
gan_generator = Generator(generator_out_layer_size)
result = gan_generator(gan_generator.get_random_input_layer()).detach()

for i in range(enzyme_count):
    input = []
    output = []
    for j in range(enzyme_size):
        input.append(-1)
        output.append(-1)
        input[j], output[j] = get_values_from_generator(j, i, enzyme_size, result[0])
    enzymes.append(Enzyme(input, output))

#enzymes = [Enzyme(Multiset(m_generator(enzyme_size)),Multiset(m_generator(enzyme_size))) for i in range(enzyme_count)]
e_generator = make_random_sequence_generator(enzymes)

sim_id = time.time()

#######################################################################
## dry run

## simulation setup - around 16 minutes in recording
samples = []
for i in range(number_of_species):
    #Todo: replace random.sample with output of generator
    s = Species(random.sample(enzymes,enzymes_per_species) ,m_generator, substrate_size)
    samples.extend([s.spawn() for i in range(number_of_samples)])
assert(len(samples)==number_of_species*number_of_samples)


## simulation execution
reactions = [s.develop(random.randint(0,max_age)) for s in samples]
print("average number of reactions", sum(reactions)/len(reactions))
max_age=int(sum(reactions)/len(reactions))

#######################################################################
## main simulation

## simulation setup
samples = []
for i in range(number_of_species):    
    s = Species(random.sample(enzymes,enzymes_per_species) ,m_generator,substrate_size)
    samples.extend([s.spawn() for i in range(number_of_samples)])
assert(len(samples)==number_of_species*number_of_samples)


## simulation execution
reactions = [s.develop(random.randint(0,max_age)) for s in samples]
print("average number of reactions", sum(reactions)/len(reactions))

## analysis of the results
corr = itertools.product(m_types,m_types) #corrleation matrix
corr = [((m1,m2),pearsonr([s.measure_metabolite_level(m1) for s in samples],[s.measure_metabolite_level(m2) for s in samples])) for m1,m2 in corr]
strong = list(filter(lambda x: x[1][1]<0.000001, corr))
print("strong correlations ",len(strong))
positive = list(filter(lambda x: x[1][0]>0, strong))
print("positive correlations ",len(positive))
negative = list(filter(lambda x: x[1][0]<0, strong))
print("negative correlations ",len(negative))
Gp = nx.Graph([e[0] for e in positive])
Gn = nx.Graph([e[0] for e in negative])
G = nx.Graph()
G.add_nodes_from(m_types)
G.add_edges_from([e[0] for e in positive], weight=1)
G.add_edges_from([e[0] for e in negative], weight=-1)

print(G.number_of_nodes())
print(G.size())
print(Gp.size())
print(Gn.size())
cc=sorted(nx.connected_components(G), key = len, reverse=True)
gcc = cc[0]
activem = set([])
for e in enzymes:
    activem.update(set(e.getproductdef()))
    activem.update(set(e.getsubstratedef()))
print("gcc ",len(gcc))
print("used metabolites ", len(activem))
print("intersection ", len(activem.intersection(gcc)))



nx.write_edgelist(G,"out/%s_G.csv"%(sim_id), comments="#", delimiter=",", data=["weight"])

random.shuffle(enzymes)


train = enzymes[:enzyme_count // 2]
train_f = open("out/%s_train.txt"%(sim_id),"w")
train_f.write(str(train))

test = enzymes[enzyme_count // 2:] + [Enzyme(Multiset(m_generator(enzyme_size)),Multiset(m_generator(enzyme_size))) for i in range(enzyme_count//2)]
random.shuffle(test)
test_f = open("out/%s_test.txt"%(sim_id),"w")
test_f.write(str(test))

enzymes = set(enzymes)
ground_truth = [e in enzymes for e in test]
ground_truth_f = open("ground_truth/%s_ground_truth.txt"%(sim_id),"w")
ground_truth_f.write(str(ground_truth))




edges = {}
for e in enzymes: 
            inputs = e.getsubstratedef()
            outputs = e.getproductdef()
            for m1 in inputs:
                for m2 in inputs:
                    w = edges.get((m1, m2),0)
                    w+=1
                    edges[m1,m2]=w
            for m1 in outputs:
                for m2 in outputs:
                    w = edges.get((m1, m2),0)
                    w+=1
                    edges[m1,m2]=w
            for m1 in inputs:
                for m2 in outputs:
                    w = edges.get((m1, m2),0)
                    w-=1
                    edges[m1,m2]=w
            for m1 in outputs:
                for m2 in inputs:
                    w = edges.get((m1, m2),0)
                    w-=1
                    edges[m1,m2]=w
edges = [(u,v,w) for (u,v),w in edges.items() if abs(w)>=2]
G_train = nx.Graph()
G_train.add_nodes_from(m_types)
for e in edges:
    G_train.add_edge(e[0], e[1], weight=e[2])
weights = [abs(w) for u,v,w in edges]


pos=nx.spring_layout(Gp)
# nx.draw(nx.difference(G_train,G),pos,
#             with_labels=False,
#             node_size=10,
#             alpha=0.5
#             )
# nx.draw(G,pos,
#             with_labels=False,
#             node_size=10,
#             alpha=0.05
#             )
nx.draw_networkx_edges(G_train,pos,
                           with_labels=False,
                           edge_color='g',
                           width=weights,
                           alpha=0.2
                        )
nx.draw_networkx_edges(Gn,pos,
                           with_labels=False,
                           edge_color='r',
                           width=1.0,
                           alpha=0.1
                        )
nx.draw_networkx_edges(Gp,pos,
                           with_labels=False,
                           edge_color='b',
                           width=1.0,
                           alpha=0.2
                        )

plt.axis('off')
plt.savefig("out/%s_vis.png"%(sim_id), bbox_inches="tight")
plt.show()
