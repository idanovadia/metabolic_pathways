import os

import torch
from openpyxl import load_workbook
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class MatrixReader:
    def __init__(self):
        #self.matrix_paths_list = ["C:\\Users\\Ido\\PycharmProjects\\metabolic_pathways\\simulator\\NN_correlation_matrix\\Original Files\\2001_fruit_pericarp_metabolite.xlsx"]
        self.matrix_paths_list = ["C:\\Users\\Ido\\PycharmProjects\\metabolic_pathways\\simulator\\NN_correlation_matrix\\Original Files\\fake_matrix.xlsx"]
        self.meta_count = -1

    #In case we want to read more than one
    def read_matrices(self):
        dataset = []
        for path in self.matrix_paths_list:
            dataset.append(self.read_matrix(path))
        return dataset

    def read_matrix(self, path):
        wb = load_workbook(path)
        sheet_name = "Sheet1"
        worksheet = wb[sheet_name]
        first_row = worksheet[1] #names_of_metabolites
        self.read_metabolites_names(first_row)

        count = self.get_metabolites_count()
        matrix = []
        for i in range(count+2):
            curr_line = []
            if i == 0 or i == 1: #skip title line
                continue
            row = worksheet[i]
            for j in range(len(row)):
                if j == 0:
                    continue
                curr_line.append(row[j].value)

            matrix.append(curr_line)

        matrix = torch.FloatTensor(matrix).to(device)
        return matrix


    def read_metabolites_names(self, first_row):
        names_dict = {}
        for i in range(len(first_row)):
            if i == 0:
                continue
            name = first_row[i].value
            names_dict[i] = name

        self.set_metabolites_conut(len(names_dict))
        self.set_metabolites_dict(names_dict)



    def set_metabolites_conut(self, count):
        self.meta_count = count

    def get_metabolites_count(self):
        return self.meta_count

    def set_metabolites_dict(self, names_dict):
        self.meta_dict = names_dict

    def get_datasize(self):
        return len(self.matrix_paths_list)