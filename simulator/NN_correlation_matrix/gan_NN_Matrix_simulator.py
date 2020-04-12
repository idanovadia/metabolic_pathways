import math
import torch.nn as nn
import torch

m_size = 50 #should not be here, just for comfort. #todo:change in future implementation

Z_dim = 100 #input layer for the generator
H_dim = 128 #middle layer
#X_dim is the output layer of generator


default_model = nn.Sequential(
            nn.Linear(Z_dim, H_dim),
            nn.ReLU(),
            nn.Linear(H_dim, 16),
            nn.Sigmoid()
        )

class Generator(nn.Module):
    def __init__(self, m_count, reaction_count, model=default_model):
        super().__init__()
        # self.model = nn.Sequential(
        #     nn.Linear(Z_dim, H_dim),
        #     nn.ReLU(),
        #     nn.Linear(H_dim, X_dim),
        #     nn.Sigmoid()
        # )
        self.model = model
        self.reaction_count = reaction_count
        self.m_count = m_count
        self.output_result = None #will determine if the gan was already activated

    def forward(self, input):
        return self.model(input)

    def get_result(self):
        z = self.get_random_input_layer()
        output = self(z)
        self.output_result = output.resize(self.reaction_count*2 ,self.m_count)

    def get_reactions_tensor(self,i):
        if(self.output_result is None):
            self.get_result()
        output = self.output_result
        #output = output.resize(2,8)
        return output[i*2],output[i*2+1]

    def get_random_input_layer(self):
        return torch.randn(1, 100)

    def turn_to_one_or_zero(self, values):
        new_values = []
        for val in values[0]:
            if val <= 0.5:
                new_values.append(0)
            else:
                new_values.append(1)
        return new_values

    def get_part_of_output(self, i, result):
        substrate = result[i*m_size*2 : i*m_size*2 + m_size]
        product = result[i*m_size*2 + m_size : i*m_size*2 + m_size + m_size]
        return substrate, product

    def set_gan_model(self, gan_model):
        self.model = gan_model

if __name__ == '__main__':
    gan_generator = Generator(2*50*10, 1)
    result = gan_generator(gan_generator.get_random_input_layer()).detach()
    result = gan_generator.turn_to_one_or_zero(result)
    result = list(range(1000))
    sub, prod = gan_generator.get_part_of_output(9,result)
