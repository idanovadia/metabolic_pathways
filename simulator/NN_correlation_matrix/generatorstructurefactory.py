#In order to create a new model your need to create a new def in
#   the class of GeneratorStructureFactory (e.g. structure_1 and create model and name for the structure.
#   return the value in this new function as a GeneratorStructure which gets name and model in init
#   Afterwards add " structure_list.append(self.yourList()) " to the function of create_strucute_list


import torch.nn as nn
Z_dim = 100 #input layer for the generator
H_dim = 128

class GeneratorStructureFactory(nn.Module):

    def __init__(self, out_dim):
        super().__init__()
        self._out_dim = out_dim
        self._structures_list = self.create_strucute_list()

    def forward(self, *input):
        raise ValueError('Should not get to forward of generator structure factory')
        pass

    def create_strucute_list(self):
        structure_list = []
        #structure_list.append(self.structure_1())
        #structure_list.append(self.structure_2())
        #structure_list.append(self.structure_3())
        #structure_list.append(self.structure_4())
        #structure_list.append(self.structure_5())
        structure_list.append(self.structure_6())
        return structure_list

    def get_structure_list(self):
        return self._structures_list

    def structure_1(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, 128),
            nn.ReLU(),
            nn.Linear(128, self._out_dim),
            nn.Sigmoid()
        )
        name = "1"
        return GeneratorStructure(name, model)

    def structure_2(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, H_dim),
            nn.ReLU(),
            nn.Linear(H_dim, H_dim * 2),
            nn.Sigmoid(),
            nn.Linear(H_dim * 2, H_dim),
            nn.ReLU(),
            nn.Linear(H_dim, self._out_dim),
            nn.Sigmoid(),
        )
        name = "2"
        return GeneratorStructure(name, model)

    def structure_3(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim*2),
            nn.Linear(Z_dim*2, Z_dim * 4),
            nn.Linear(Z_dim*4, Z_dim * 2),
            nn.Linear(Z_dim*2, self._out_dim),
        )
        name = "3"
        return GeneratorStructure(name, model)

    def structure_4(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim*2),
            nn.Linear(Z_dim*2, Z_dim * 4),
            nn.Linear(Z_dim*4, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Linear(Z_dim*4, Z_dim * 2),
            nn.Linear(Z_dim*2, self._out_dim),
        )
        name = "4"
        return GeneratorStructure(name, model)

    def structure_5(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim*2),
            nn.Linear(Z_dim*2, Z_dim * 4),
            nn.Linear(Z_dim*4, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim * 16),
            nn.Linear(Z_dim * 16, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Linear(Z_dim*4, Z_dim * 2),
            nn.Linear(Z_dim*2, self._out_dim),
        )
        name = "5"
        return GeneratorStructure(name, model)

    def structure_6(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim * 2),
            nn.ReLU(),
            nn.Linear(Z_dim * 2, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 4, Z_dim * 8),
            nn.ReLU(),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 4, Z_dim * 2),
            nn.ReLU(),
            nn.Linear(Z_dim * 2, self._out_dim),
            nn.Sigmoid(),
        )
        name = "6"
        return GeneratorStructure(name, model)


class GeneratorStructure():

    def __init__(self, name, model):
        self._name = name
        self._model = model

    def get_model(self):
        return self._model

    def get_name(self):
        return self._name

    #todo: maybe change in future because of multireaction
    def set_score(self, input_error, out_error):
        self.input_error = input_error
        self.out_error = out_error

    def get_score(self):
        return self.input_error, self.out_error






