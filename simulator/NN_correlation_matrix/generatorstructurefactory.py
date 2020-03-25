#In order to create a new model your need to create a new def in
#   the class of GeneratorStructureFactory (e.g. structure_1 and create model and name for the structure.
#   return the value in this new function as a GeneratorStructure which gets name and model in init
#   Afterwards add " structure_list.append(self.yourList()) " to the function of create_strucute_list


import torch.nn as nn
Z_dim = 100 #input layer for the generator

class GeneratorStructureFactory(nn.Module):

    def __init__(self, out_dim):
        super().__init__()
        self._out_dum = out_dim
        self._structures_list = self.create_strucute_list()

    def forward(self, *input):
        raise ValueError('Should not get to forward of generator structure factory')
        pass

    def create_strucute_list(self):
        structure_list = []
        structure_list.append(self.structure_1())
        structure_list.append(self.structure_2())
        return structure_list

    def get_structure_list(self):
        return self._structures_list

    def structure_1(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, 128),
            nn.ReLU(),
            nn.Linear(128, self._out_dum),
            nn.Sigmoid()
        )
        name = "1"
        return GeneratorStructure(name, model)

    def structure_2(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, 128),
            nn.ReLU(),
            nn.Linear(128, self._out_dum),
            nn.Sigmoid()
        )
        name = "2"
        return GeneratorStructure(name, model)


class GeneratorStructure():

    def __init__(self, name, model):
        self._name = name
        self._model = model

    def get_model(self):
        return self._model

    def get_name(self):
        return self._name






