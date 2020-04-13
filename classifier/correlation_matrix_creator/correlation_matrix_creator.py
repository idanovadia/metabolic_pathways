import pandas as pd
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from configparser import ConfigParser
import numpy as np


class CorrMaxtrix(AbstractConfigClass):
    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.input_file_path = self.getPath(self.config_parser.eval(self.__class__.__name__,"input_file_path"))
        self.output_path_folder = self.getPath(self.config_parser.eval(self.__class__.__name__, "output_path_folder"))
        self.pearsonCorr = ""
        self.output_file_name = str(self.input_file_path).split(sep="/")[-1]

    def exec(self):
        self.corr()
        # self.powerCorrMatrix(2)
        self.saveFile()

    def corr(self):
        profile = pd.read_excel(self.input_file_path, index_col=0, header=0)
        profile = profile.drop([profile.index[0]]).T
        profile= profile.astype(float)
        self.pearsonCorr = profile.corr(method='pearson')

    def saveFile(self):
        self.pearsonCorr.to_excel(self.output_path_folder + "/" + self.output_file_name)

    def powerCorrMatrix(self,p):
        self.pearsonCorr = np.power((self.pearsonCorr.to_numpy()),p)