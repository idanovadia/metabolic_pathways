import pandas as pd
import numpy as np
import sklearn

'''
This class using for preprocessing xls files
'''
class Preprocessing:
    def __init__(self, file_path,dir_out_path):
        self.path = file_path
        self.csv_pd_out = ""
        self.dir_out_path = dir_out_path
        self.out_name = str(file_path).split(sep="\\")[-1]

    '''
    put mean in each na's cells use the mean of the row.
    '''
    def fillNaToMean(self):
        csv_pd = pd.read_excel(self.path, index_col=0, header=0)
        print(csv_pd.head())
        csv_pd_T = csv_pd.T
        for index, row in enumerate(csv_pd_T):
            if index == 0:
                continue
            csv_pd_T[row] = csv_pd_T[row].fillna(csv_pd_T[row].mean())
        self.csv_pd_out = csv_pd_T.T

    '''
    save xls file to specific dir. 
    '''
    def saveFile(self):
        self.csv_pd_out.to_excel(self.dir_out_path+"\\out_" + self.out_name)
