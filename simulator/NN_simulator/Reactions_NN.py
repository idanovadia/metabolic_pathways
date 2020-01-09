#!/usr/bin/env python
# coding: utf-8

# In[3]:


import torch
import torch.nn.functional as F
import random
import copy
import time


# In[2]:
from simulator.NN_simulator.gan_NN_simulator import Generator


def generate_reaction_def(sub_count, prod_count, metabolites, low=0, high=1):
    """
    returns a tupple (substrate, product) of sub_count substrates randomly drawn from metabolites
    and prod_count products randomly drawn from metabolites 
    """
    m = set(metabolites)
    sub = set(random.sample(m,sub_count))
    prod = set(random.sample(m,prod_count))
    return ([random.uniform(low,high) if i in sub else 0.0 for i in m], 
            [random.uniform(low,high) if i in prod else 0.0 for i in m])
    
    


# In[3]:


class Reaction(torch.nn.Module):
    def __init__(self,sub,prod,eps=1e-20,step=0.0001):
        super(Reaction,self).__init__()
        self._sub = torch.nn.Parameter(sub.clone())
        self._prod = torch.nn.Parameter(prod.clone())
        self._step = step
        self._eps = eps

    def forward(self, x):
        y = x
        x = x / self._sub #required sub
        x = 1-1/x         #the chance to collect all required substrates
        x = F.relu(x)     #nullify negative prob
        x = x.prod(dim=1,keepdim=True) #total prob to collect all required substrates
        x = x * self._step
        x = y + x*(self._prod - self._sub)
        return x
    
    def get_def_tensor(self):
        s = torch.unsqueeze(self._sub,0)
        p = torch.unsqueeze(self._prod,0)
        return torch.cat((s,p),dim=0)
    
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return "Reaction(\n\tsub={},\n\t prod={})".format(self._sub,self._prod)


# In[4]:


class MultiReaction(torch.nn.Module):
    def __init__(self,rcount,metabolites,scount=2,pcount=2,step=0.0001,low=0.0, high=1.0):
        super(MultiReaction,self).__init__()
        self._reactions = torch.nn.ModuleList()
        for i in range(rcount):
            sub,prod = generate_reaction_def(scount,pcount,metabolites,low,high)
            sub = torch.Tensor(sub).to(device)#so far there is no self.device in pytorch Modules
            prod = torch.Tensor(prod).to(device)#so far there is no self.device in pytorch Modules
            r = Reaction(sub,prod,step=step)
            self._reactions.append(r)

    def forward(self, x):
        #random.shuffle(self._reactions)
        for m in self._reactions:
            x = m(x)
        return x
    
    def get_reactions_tensor(self):        
        rslt = [r.get_def_tensor().unsqueeze(dim=0) for r in self._reactions]
        rslt = torch.cat(rslt,dim=0)
        return rslt


# In[23]:


def pearson_r(x,y):
    vx = x - torch.mean(x)    
    vy = y - torch.mean(y)
    
    rx = torch.rsqrt(torch.sum(vx ** 2))    
    ry = torch.rsqrt(torch.sum(vy ** 2))
    
    s = torch.sum(vx * vy)
    cost = s * rx * ry
    return cost

def correlation_matrix(b):
    vb = b - torch.mean(b,dim=0)
    mr = torch.rsqrt(torch.sum(vb ** 2, dim=0))
    mr.unsqueeze_(dim=0)
    corr = torch.mm(vb.t(),vb) * torch.mm(mr.t(),mr)
    return corr


# In[5]:

#rcount is like enzyme_count in the metasim file
class Process(torch.nn.Module): #model
    def __init__(self,rcount,metabolites,scount=2,pcount=2,step=0.0001,iterations=100,low=0.0,high=1.0):
        super(Process,self).__init__()
        self._mr = MultiReaction(rcount,metabolites,scount=scount,pcount=pcount,step=step,low=low,high=high)
        self._iterations = iterations
        
    def forward(self, x):
        for i in range(self._iterations):
            x = self._mr(x) 
        
        #x = correlation_matrix(x)
        
        return x
    
    def get_reactions_tensor(self):
        return self._mr.get_reactions_tensor()
    


# In[6]:


import numpy as np
import sklearn.cluster as cluster

def compare_tensor_sets(s1,s2): 
    """
    s1 and s2 are lists of tensors of the same size and shape. 
    the comparison is performed in a greedy manner where the frist element of s1 is compared to all elements of s2,
    the minimal MSE is recorded, and the respective element of s2 is removed. The second element of s1 is compared
    to the remaining elements of s2 and so on. 
    @return the average of the minimal MSE values for all elements of s1.  
    """
    s1 = list(s1)
    s2 = list(s2)
    rcount = len(s1)
    assert(rcount==len(s2))
    rslt = 0.0
    while len(s1)>0:
        i = s1.pop()
        mses = torch.Tensor([F.mse_loss(i,j) for j in s2])
        j = mses.argmin()
        del s2[j]
        rslt+=mses[j]    
    return rslt / rcount


# In[7]:


m_count = 50 #number of metabolis
reactions_count = 10
dataset_size = 1#500 #generated x,y
minibatch_size = 10000
sub_min = 2.0001
sub_max = 10.0
epochs = 500
step = 0.01
iterations = 20
s_count=10
p_count=10

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") 
#device = "cpu"


# In[8]:


metabolites = range(m_count)
reactions = Process(reactions_count, metabolites, 
                    scount=s_count, pcount=p_count, 
                    step=step, iterations=iterations,
                    low=1.0,high=1.0
                   ).to(device)


# In[9]:


with torch.no_grad():
    dataset = []
    for i in range(dataset_size):
        batch_x = torch.Tensor(size=(minibatch_size,m_count)).to(device)
        batch_x.uniform_(sub_min,sub_max)
        batch_y = reactions(batch_x)
        dataset.append((batch_x,batch_y))
        if i%1==0:
            r = (dataset[-1][1]-dataset[-1][0]).abs().sum(dim=1).neg()
            print("{}:{}".format(i,F.threshold(r,threshold=-1e-20,value=1).sum()))


# In[10]:

gan_generator = Generator( (2*m_count) * reactions_count)
result = gan_generator(gan_generator.get_random_input_layer()).detach()
result = gan_generator.turn_to_one_or_zero(result)
model = Process(reactions_count, metabolites,scount=m_count, pcount=m_count, step=step,iterations=iterations).to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
g_optimizer = torch.optim.Adam(gan_generator.parameters(), lr=1e-3)
##optimizer = torch.optim.Adadelta(model.parameters(), lr=1.0, rho=0.9, eps=1e-06, weight_decay=1.0)
##optimizer = torch.optim.Adagrad(model.parameters(), lr=0.01, lr_decay=0, weight_decay=0, initial_accumulator_value=0)
#optimizer = torch.optim.Adamax(model.parameters(), lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
#optimizer = torch.optim.ASGD(model.parameters(), lr=0.1, lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0.01)
#optimizer = torch.optim.SGD(model.parameters(), lr=0.1, momentum=0.9, dampening=0, weight_decay=0, nesterov=False)


ploss=0.0
rloss=0.0
with torch.no_grad():
    rt = reactions.get_reactions_tensor()
    r1 = model.get_reactions_tensor()
T = time.time()
for epoch in range(epochs): #training. Around 22 minutes in recording 31/12/19. 
    for x,y in dataset:
        
        optimizer.zero_grad()

        y_pred = model(x)
        loss = F.mse_loss(y_pred, y)        
        loss.backward(retain_graph=True)
        optimizer.step() #this optimizer is for the original model
        
        #print(y_pred)
        #print(y)
        #print(loss)
        
        with torch.no_grad():
            r2=model.get_reactions_tensor()
            if (ploss>0) and (loss.item() / ploss > 100): 
                print(r1)
                print(r2)
            ploss += float(loss.item())
            rloss += float(compare_tensor_sets(rt, r2).item())
            r1 = r2
            
    if epoch % 1 == 0:
        T = time.time() - T
        ploss = ploss / 1 / dataset_size
        rloss = rloss / 1 / dataset_size
        print("{}\t time:{:2.3g} \t p-loss:{} \t r-loss :{}".format(epoch,T,ploss,rloss))
        if ploss < (10**(-20)):
            print("stop")
            break
        ploss=0.0
        rloss=0.0
        T = time.time()


# In[12]:


predicted = model.get_reactions_tensor()
predicted = ((predicted*10).round()/10).int()
predicted = [repr(t) for t in list(predicted)]
predicted.sort()


original = reactions.get_reactions_tensor().int()
original = [repr(t) for t in list(original)]
original.sort()

verdict = [x==y for x,y in zip(original, predicted)]
print(verdict)

for i in range(len(predicted)): 
    print("reaction %d predicted: %r "%(i,original[i]==predicted[i]))
    print("original:")
    print(original[i])
    print("predicted:")
    print(predicted[i])


# In[ ]:




