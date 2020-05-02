#In order to create a new model your need to create a new def in
#   the class of GeneratorStructureFactory (e.g. structure_1 and create model and name for the structure.
#   return the value in this new function as a GeneratorStructure which gets name and model in init
#   Afterwards add " structure_list.append(self.yourList()) " to the function of create_strucute_list

import torch
import torch.nn as nn

Z_dim = 100 #input layer for the generator
H_dim = 128

global device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

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
        # structure_list.append(self.structure_1())
        # structure_list.append(self.structure_2())
        # structure_list.append(self.structure_3())
        # structure_list.append(self.structure_4())
        # structure_list.append(self.structure_5())
        # structure_list.append(self.structure_6())
        # structure_list.append(self.structure_7())
        # structure_list.append(self.structure_8())
        # structure_list.append(self.structure_9())
        # structure_list.append(self.structure_10())
        structure_list.append(self.structure_11())
        # structure_list.append(self.structure_12())
        # structure_list.append(self.structure_13())
        # structure_list.append(self.structure_14())
        # structure_list.append(self.structure_15())

        # for i in range(10):
        #     structure = self.structure_11()
        #     structure.set_name("model 11 (" + str(i) + ")")
        #     structure_list.append(structure)

        return structure_list

    def get_structure_list(self):
        return self._structures_list

    #Input Error Score: 50.0%. Output Error Score: 62.5%
    def structure_1(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, 128),
            nn.ReLU(),
            nn.Linear(128, self._out_dim),
            nn.Sigmoid()
        )
        name = "1"
        return GeneratorStructure(name, model)

    #Input Error Score: 62.5%. Output Error Score: 62.5%
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

    #Input Error Score: 37.5%. Output Error Score: 37.5%
    def structure_3(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim*2),
            nn.Linear(Z_dim*2, Z_dim * 4),
            nn.Linear(Z_dim*4, Z_dim * 2),
            nn.Linear(Z_dim*2, self._out_dim),
        )
        name = "3"
        return GeneratorStructure(name, model)

    #Input Error Score: 37.5%. Output Error Score: 37.5%
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

    #Input Error Score: 75.0%. Output Error Score: 50.0%
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

    #based on model 4, but with Relu and sigmoid functions
    # Input Error Score: 75.0%. Output Error Score: 87.5%
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

    #based on model 5 but with relu and sigmoid fucntions
    #Input Error Score: 75.0%. Output Error Score: 87.5%
    def structure_7(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim*2),
            nn.ReLU(),
            nn.Linear(Z_dim*2, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim*4, Z_dim * 8),
            nn.ReLU(),
            nn.Linear(Z_dim * 8, Z_dim * 16),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 16, Z_dim * 8),
            nn.ReLU(),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim*4, Z_dim * 2),
            nn.ReLU(),
            nn.Linear(Z_dim*2, self._out_dim),
            nn.Sigmoid(),
        )
        name = "7"
        return GeneratorStructure(name, model)

    #based on model 4, but with Relu function
    #Input Error Score: 87.5%. Output Error Score: 62.5%
    def structure_8(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim * 2),
            nn.ReLU(),
            nn.Linear(Z_dim * 2, Z_dim * 4),
            nn.ReLU(),
            nn.Linear(Z_dim * 4, Z_dim * 8),
            nn.ReLU(),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.ReLU(),
            nn.Linear(Z_dim * 4, Z_dim * 2),
            nn.ReLU(),
            nn.Linear(Z_dim * 2, self._out_dim),
            nn.Sigmoid(),
        )
        name = "8"
        return GeneratorStructure(name, model)

    # based on model 4, but with sigmoid function
    #Input Error Score: 50.0%. Output Error Score: 87.5%
    def structure_9(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim * 2),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 2, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 4, Z_dim * 8),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 4, Z_dim * 2),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 2, self._out_dim),
            nn.Sigmoid(),
        )
        name = "9"
        return GeneratorStructure(name, model)

    #based on model 5 but with sigmoid fucntion
    #Input Error Score: 12.5%. Output Error Score: 37.5%
    def structure_10(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim*2),
            nn.Sigmoid(),
            nn.Linear(Z_dim*2, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim*4, Z_dim * 8),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 8, Z_dim * 16),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 16, Z_dim * 8),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim*4, Z_dim * 2),
            nn.Sigmoid(),
            nn.Linear(Z_dim*2, self._out_dim),
            nn.Sigmoid(),
        )
        name = "10"
        return GeneratorStructure(name, model)

    #based on model 4 but with one sigmoid function
    #Input Error Score: 50.0%. Output Error Score: 25.0%
    def structure_11(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim * 2),
            nn.Linear(Z_dim * 2, Z_dim * 4),
            nn.Linear(Z_dim * 4, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Linear(Z_dim * 4, Z_dim * 2),
            nn.Linear(Z_dim * 2, self._out_dim),
            nn.Sigmoid(),
        )
        name = "11"
        return GeneratorStructure(name, model)

    def structure_12(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim * 2),
            nn.Linear(Z_dim * 2, Z_dim * 4),
            nn.Linear(Z_dim * 4, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim * 16),
            nn.Linear(Z_dim * 16, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Linear(Z_dim * 4, Z_dim * 2),
            nn.Linear(Z_dim * 2, self._out_dim),
            nn.Sigmoid(),
        )
        name = "12"
        return GeneratorStructure(name, model)

    def structure_13(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim * 2),
            nn.Linear(Z_dim * 2, Z_dim * 4),
            nn.Linear(Z_dim * 4, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim * 16),
            nn.Linear(Z_dim * 16, Z_dim * 32),
            nn.Linear(Z_dim * 32, Z_dim * 16),
            nn.Linear(Z_dim * 16, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Linear(Z_dim * 4, Z_dim * 2),
            nn.Linear(Z_dim * 2, self._out_dim),
            nn.Sigmoid(),
        )
        name = "13"
        return GeneratorStructure(name, model)

    def structure_14(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim * 32),
            nn.Linear(Z_dim * 32, Z_dim * 64),
            nn.Linear(Z_dim * 64, Z_dim * 128),
            nn.Linear(Z_dim * 128, Z_dim * 64),
            nn.Linear(Z_dim * 64, Z_dim * 32),
            nn.Linear(Z_dim * 32, Z_dim * 8),
            nn.Linear(Z_dim * 8, Z_dim),
            nn.Linear(Z_dim, self._out_dim),
            nn.Sigmoid(),
        )
        name = "14"
        return GeneratorStructure(name, model)

    #based on 11, but with sigmoid between each layer
    def structure_15(self):
        model = nn.Sequential(
            nn.Linear(Z_dim, Z_dim * 2),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 2, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 4, Z_dim * 8),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 8, Z_dim * 4),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 4, Z_dim * 2),
            nn.Sigmoid(),
            nn.Linear(Z_dim * 2, self._out_dim),
            nn.Sigmoid(),
        )
        name = "15"
        return GeneratorStructure(name, model)


class GeneratorStructure():

    def __init__(self, name, model):
        self._name = name
        self._model = model
        self._model = model.to(device)
        self.original_reactions = []
        self.predicted_reactions = []

    def get_model(self):
        return self._model

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_score(self, input_error, out_error):
        self.input_error_dict = input_error
        self.out_error_dict = out_error

    def get_score(self):
        return self.input_error_dict, self.out_error_dict

    def set_last_mse_loss(self, mse_loss):
        self.mse_loss = mse_loss

    def get_last_mse_loss(self):
        return self.mse_loss

    def add_to_original_reactions_list(self, reaction):
        self.original_reactions.append(reaction)

    def add_to_predicted_reactions_list(self, reaction):
        self.predicted_reactions.append(reaction)

    def get_reactions_lists(self):
        return self.original_reactions, self.predicted_reactions






