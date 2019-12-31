import torch.nn as nn
import torch


Z_dim = 100 #input layer for the generator
H_dim = 128 #middle layer
#X_dim is the output layer of generator

class Generator(nn.Module):
    def __init__(self, X_dim):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(Z_dim, H_dim),
            nn.ReLU(),
            nn.Linear(H_dim, X_dim),
            nn.Sigmoid()
        )

    def forward(self, input):
        return self.model(input)

    def get_random_input_layer(self):
        return torch.randn(1, 100)


