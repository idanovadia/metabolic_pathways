import torch
import torch.optim as opt
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline


mb_size = 64

transform = transforms.ToTensor()

trainData = torchvision.datasets.MNIST('./data/', download=True, transform=transform, train=True)

trainLoader = torch.utils.data.DataLoader(trainData, shuffle=True, batch_size=mb_size)

dataIter = iter(trainLoader)

imgs, labels = dataIter.next()

def imshow(imgs):
    imgs = torchvision.utils.make_grid(imgs)
    npimgs = imgs.numpy()
    plt.figure(figsize=(8,8))
    plt.imshow(np.transpose(npimgs, (1,2,0)), cmap='Greys_r')
    plt.xticks([])
    plt.yticks([])
    plt.show()

Z_dim = 100
H_dim = 128
X_dim = imgs.view(imgs.size(0), -1).size(1)


class Gen(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(Z_dim, H_dim),
            nn.ReLU(),
            nn.Linear(H_dim, X_dim),
            nn.Sigmoid()
        )

    def forward(self, input):
        return self.model(input)

G = Gen()

class Dis(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(X_dim, H_dim),
            nn.ReLU(),
            nn.Linear(H_dim, 1),
            nn.Sigmoid()
        )

    def forward(self, input):
        return self.model(input)

D = Dis()

lr = 1e-3 #learning rate

g_opt = opt.Adam(G.parameters(), lr=lr)
d_opt = opt.Adam(D.parameters(), lr=lr)

def train(num_epchos):
    for epoch in range(num_epchos):
        G_loss_run = 0.0
        D_loss_run = 0.0

        #todo: change the data to our data
        for i, data in enumerate(trainLoader): #we need to replace this data with the data that the discriminator is trained with
            X, _ = data
            X = X.view(X.size(0), -1) #convert the data to another form, nto sure about it
            mb_size = X.size(0) #batch size

            one_labels = torch.ones(mb_size, 1)
            zero_labels = torch.zeros(mb_size, 1)

            # Random noise for Generator. Z_dim is the vector of noise that is the input for the generator
            z = torch.randn(mb_size, Z_dim)

            #Results of the discriminator with the real input X
            D_real = D(X)
            #Results of the discriminator with generator input
            #todo: first of all get the result from the G(z), run it through the simulator
            D_fake = D(G(z))

            D_real_loss = F.binary_cross_entropy(D_real, one_labels) #For every real data output should  be one in discriminator
            D_fake_loss = F.binary_cross_entropy(D_fake, zero_labels) #For every fake data output should  be zero in discriminator
            D_loss = D_real_loss + D_fake_loss

            #Start back propagation for discrimination
            d_opt.zero_grad()
            D_loss.backward()
            d_opt.step()

            z = torch.randn(mb_size, Z_dim) #take new noise
            D_fake = D(G(z)) #output of discriminator for fake data
            G_loss = F.binary_cross_entropy(D_fake, one_labels) #Ideally, we want that every D_fake result will be one

            # Start back propagation for generator
            g_opt.zero_grad()
            G_loss.backward()
            g_opt.step()

            G_loss_run += G_loss.item()
            D_loss_run += D_loss.item()

        print('Epoch:{},   G_loss:{},    D_loss:{}'.format(epoch, G_loss_run / (i + 1), D_loss_run / (i + 1)))

        samples = G(z).detach()
        samples = samples.view(samples.size(0), 1, 28, 28).cpu()
        imshow(samples)

if __name__ == '__main__':
    train(20)