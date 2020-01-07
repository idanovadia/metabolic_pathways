import pandas as pd
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from configparser import ConfigParser
import numpy as np
import sklearn

'''
This class using for preprocessing xls files
'''
class Preprocessing(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        '''
          put mean in each na's cells use the mean of the row.
          '''
        self.input_file_path = self.getPath(relative_path=self.config_parser.eval(self.__class__.__name__,"input_file_path"))
        self.output_path_folder = self.getPath((self.config_parser.eval(self.__class__.__name__,"output_path_folder")))
        self.output_file_name = str(self.input_file_path).split(sep="/")[-1]

    def exec(self):
        self.fillNaToMean()
        self.saveFile()


    def fillNaToMean(self):
        csv_pd = pd.read_excel(self.input_file_path, index_col=0, header=0)
        print(csv_pd.head())
        csv_pd_T = csv_pd.T
        csv_pd_T = csv_pd_T.fillna(0)
        # for index, row in enumerate(csv_pd_T):
        #     if index == 0:
        #         continue
        #     csv_pd_T[row] = csv_pd_T[row].fillna(csv_pd_T[row].mean())
        self.csv_pd_out = csv_pd_T.T

    '''
    save xls file to specific dir. 
    '''
    def saveFile(self):
        self.csv_pd_out.to_excel(self.output_path_folder+"/" + self.output_file_name)
