import random
import itertools
from multiset import Multiset
from scipy.stats import pearsonr
import networkx as nx
import matplotlib.pyplot as plt
import copy
import time


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
enzymes_per_species = 80
substrate_size = 10000
number_of_samples = 1
number_of_species = 100
max_age = 10000

m_types = range(mtype_count)
m_generator = make_random_sequence_generator(m_types)
enzymes = [Enzyme(Multiset(m_generator(enzyme_size)),Multiset(m_generator(enzyme_size))) for i in range(enzyme_count)]
e_generator = make_random_sequence_generator(enzymes)

sim_id = time.time()

#######################################################################
## dry run

## simulation setup - around 16 minutes in recording
samples = []
for i in range(number_of_species):    
    s = Species(random.sample(enzymes,enzymes_per_species) ,m_generator,substrate_size)
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
corr = itertools.product(m_types,m_types)
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
    G_train.add_edge(e[0], e[1], {'weight':e[2]})     
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

###############################################################################################################

import tensorflow as tf
import numpy as np

def generator(z, out_channel_dim, is_train=True):
    """
    Create the generator network
    """
    alpha = 0.2

    with tf.variable_scope('generator', reuse=False if is_train == True else True):
        # First fully connected layer
        x_1 = tf.layers.dense(z, 2 * 2 * 512)

        # Reshape it to start the convolutional stack
        deconv_2 = tf.reshape(x_1, (-1, 2, 2, 512))
        batch_norm2 = tf.layers.batch_normalization(deconv_2, training=is_train)
        lrelu2 = tf.maximum(alpha * batch_norm2, batch_norm2)

        # Deconv 1
        deconv3 = tf.layers.conv2d_transpose(lrelu2, 256, 5, 2, padding='VALID')
        batch_norm3 = tf.layers.batch_normalization(deconv3, training=is_train)
        lrelu3 = tf.maximum(alpha * batch_norm3, batch_norm3)

        # Deconv 2
        deconv4 = tf.layers.conv2d_transpose(lrelu3, 128, 5, 2, padding='SAME')
        batch_norm4 = tf.layers.batch_normalization(deconv4, training=is_train)
        lrelu4 = tf.maximum(alpha * batch_norm4, batch_norm4)

        # Output layer
        logits = tf.layers.conv2d_transpose(lrelu4, out_channel_dim, 5, 2, padding='SAME')

        out = tf.tanh(logits)

        return out


def discriminator(images, reuse=False):
    """
    Create the discriminator network
    """
    alpha = 0.2

    with tf.variable_scope('discriminator', reuse=reuse):
        # using 4 layer network as in DCGAN Paper

        # Conv 1
        conv1 = tf.layers.conv2d(images, 64, 5, 2, 'SAME')
        lrelu1 = tf.maximum(alpha * conv1, conv1)

        # Conv 2
        conv2 = tf.layers.conv2d(lrelu1, 128, 5, 2, 'SAME')
        batch_norm2 = tf.layers.batch_normalization(conv2, training=True)
        lrelu2 = tf.maximum(alpha * batch_norm2, batch_norm2)

        # Conv 3
        conv3 = tf.layers.conv2d(lrelu2, 256, 5, 1, 'SAME')
        batch_norm3 = tf.layers.batch_normalization(conv3, training=True)
        lrelu3 = tf.maximum(alpha * batch_norm3, batch_norm3)

        # Flatten
        flat = tf.reshape(lrelu3, (-1, 4 * 4 * 256))

        # Logits
        logits = tf.layers.dense(flat, 1)

        # Output
        out = tf.sigmoid(logits)

        return out, logits


def model_inputs(image_width, image_height, image_channels, z_dim):
    """
    Create the model inputs
    """
    inputs_real = tf.placeholder(tf.float32, shape=(None, image_width, image_height, image_channels), name='input_real')
    inputs_z = tf.placeholder(tf.float32, (None, z_dim), name='input_z')
    learning_rate = tf.placeholder(tf.float32, name='learning_rate')

    return inputs_real, inputs_z, learning_rate


def model_loss(input_real, input_z, out_channel_dim):
    """
    Get the loss for the discriminator and generator
    """

    label_smoothing = 0.9

    g_model = generator(input_z, out_channel_dim)
    d_model_real, d_logits_real = discriminator(input_real)
    d_model_fake, d_logits_fake = discriminator(g_model, reuse=True)

    d_loss_real = tf.reduce_mean(
        tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_real,
                                                labels=tf.ones_like(d_model_real) * label_smoothing))
    d_loss_fake = tf.reduce_mean(
        tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_fake,
                                                labels=tf.zeros_like(d_model_fake)))

    d_loss = d_loss_real + d_loss_fake

    g_loss = tf.reduce_mean(
        tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_fake,
                                                labels=tf.ones_like(d_model_fake) * label_smoothing))

    return d_loss, g_loss

def model_opt(d_loss, g_loss, learning_rate, beta1):
    """
    Get optimization operations
    """
    t_vars = tf.trainable_variables()
    d_vars = [var for var in t_vars if var.name.startswith('discriminator')]
    g_vars = [var for var in t_vars if var.name.startswith('generator')]

    # Optimize
    with tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS)):
        d_train_opt = tf.train.AdamOptimizer(learning_rate, beta1=beta1).minimize(d_loss, var_list=d_vars)
        g_train_opt = tf.train.AdamOptimizer(learning_rate, beta1=beta1).minimize(g_loss, var_list=g_vars)

    return d_train_opt, g_train_opt

def show_generator_output(sess, n_images, input_z, out_channel_dim):
    """
    Show example output for the generator
    """
    z_dim = input_z.get_shape().as_list()[-1]
    example_z = np.random.uniform(-1, 1, size=[n_images, z_dim])

    samples = sess.run(
        generator(input_z, out_channel_dim, False),
        feed_dict={input_z: example_z})

    #pyplot.imshow(helper.images_square_grid(samples))
    #pyplot.show()

def train(epoch_count, batch_size, z_dim, learning_rate, beta1, get_batches, data_shape):
    """
    Train the GAN
    """
    input_real, input_z, _ = model_inputs(data_shape[1], data_shape[2], data_shape[3], z_dim)
    d_loss, g_loss = model_loss(input_real, input_z, data_shape[3])
    d_opt, g_opt = model_opt(d_loss, g_loss, learning_rate, beta1)

    steps = 0

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch_i in range(epoch_count):
            for batch_images in get_batches(batch_size):

                # values range from -0.5 to 0.5, therefore scale to range -1, 1
                batch_images = batch_images * 2
                steps += 1

                batch_z = np.random.uniform(-1, 1, size=(batch_size, z_dim))

                _ = sess.run(d_opt, feed_dict={input_real: batch_images, input_z: batch_z})
                _ = sess.run(g_opt, feed_dict={input_real: batch_images, input_z: batch_z})

                if steps % 400 == 0:
                    # At the end of every 10 epochs, get the losses and print them out
                    train_loss_d = d_loss.eval({input_z: batch_z, input_real: batch_images})
                    train_loss_g = g_loss.eval({input_z: batch_z})

                    print("Epoch {}/{}...".format(epoch_i + 1, epoch_count), #epoch_count was just epochs, there was an error
                          "Discriminator Loss: {:.4f}...".format(train_loss_d),
                          "Generator Loss: {:.4f}".format(train_loss_g))

                    _ = show_generator_output(sess, 1, input_z, data_shape[3])