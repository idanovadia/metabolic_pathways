#Class to process results from the output of the trained model
#also in charge of providing the classifier with proper files

import torch
import matplotlib.pyplot as plt
from openpyxl.drawing.image import Image
from openpyxl import Workbook, load_workbook

global device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")



class ResultProcessor:

    def __init__(self, m_count, minibatch_size, sub_min, sub_max):
        self.saving_path ="Results/"
        self.outputs_path = self.saving_path + "\\Saved Models\\Outputs"
        self.model = None
        self.m_count = m_count
        self.minibatch_size = minibatch_size
        self.sub_min = sub_min
        self.sub_max = sub_max


    def load_model(self, name):
        #model = Process_new(self.reactions_count, self.metabolites, self.m_count, self.m_count, self.iterations)
        #model.load_state_dict()
        model = torch.load(self.saving_path + "\\Saved Models\\" + name)
        model.eval()
        self.model = model

    def run_model(self):
        rand_x = torch.Tensor(size=(self.minibatch_size, self.m_count))
        rand_x.uniform_(self.sub_min, self.sub_max)
        rand_x = rand_x.to(device)

        # ym, yc = model(x)
        ym, yc = self.model(rand_x)
        self.draw_matrix(yc,0)

        reactions = self.model.get_reactions_tensor()
        self.write_reactions_data(reactions)

        matrix = yc.detach().numpy()
        self.write_matrix_data(matrix)

    #write matrix data to excel
    def write_matrix_data(self, matrix):
        wb = Workbook()
        sheet_name = "matrix"
        wb.create_sheet(sheet_name, 0)
        active = wb[sheet_name]

        #adding first raw of metabolites name
        metabolites = list(range(self.m_count))
        metabolites = ["X"] + metabolites #we insert 'X' so the table will look good
        line_append = metabolites
        active.append(line_append)

        for i in range(len(matrix)):
            line_append = [i] + matrix[i].tolist()
            active.append(line_append)

        wb.save(self.outputs_path + "\\result_p.xlsx")

    def draw_matrix(self, model_output, id):
        filepath = self.outputs_path + "\\matrix" + str(id) + ".png"
        color = "YlGnBu"
        dpi_size = 100
        wb = Workbook()
        sheet_name = "matrix visual"

        # Create the matrix for yc result
        plt.close()
        plt.title('correlation matrix created by model')
        npimg = model_output.detach().cpu().numpy()
        plt.imshow(npimg, cmap=color)
        plt.savefig(filepath, dpi=dpi_size)

        # Add photos to excel sheet
        # Activate worksheet
        wb.create_sheet(sheet_name, 0)
        active = wb[sheet_name]

        # Insert plot into worksheet
        # Select active sheet and cell reference
        img = Image(filepath)
        active.add_image(img, 'A1')

        wb.save(self.outputs_path + "\\result_p.xlsx")

    def get_saving_path(self):
        return self.saving_path

    def set_model(self, model):
        self.model = model

    #Write each reaction to a different excel file
    def write_reactions_data(self, reactions):
        reactions = reactions.round().int()
        print(reactions)
        for i in range(len(reactions)):
            reaction = reactions[i]
            wb = Workbook()
            sheet_name = "reaction" + str(i)
            wb.create_sheet(sheet_name, 0)
            active = wb[sheet_name]

            metabolic_list_num = []
            for j in range(self.m_count):
                if reaction[0][j] == 1:
                    metabolic_list_num.append(j)
                elif reaction[1][j] == 1: #doing else if because we don't want to add same metabolic twice
                    metabolic_list_num.append(j)

            metabolic_list = self.turn_metabolic_id_to_name(metabolic_list_num)

            line_append = metabolic_list_num #todo: change from metabolic_list_num to metabolic_list
            active.append(line_append)
            wb.save(self.outputs_path + "\\Reactions\\reaction" + str(i) + ".xlsx")

    #todo: complete this
    def turn_metabolic_id_to_name(self, metabolic_list_num):
        pass
