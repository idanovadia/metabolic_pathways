import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sb

class CorrMaxtrix:
    def __init__(self, file_path, dir_out_path):
        self.file_path = file_path
        self.dir_out_path = dir_out_path
        self.pearsonCorr = ""
        self.out_name = str(file_path).split(sep="\\")[-1]

    def corr(self):
        profile = pd.read_excel(self.file_path, index_col=0, header=0)
        profile = profile.drop([profile.index[0]]).T
        profile= profile.astype(float)
        self.pearsonCorr = profile.corr(method='pearson')

    def saveFile(self):
        self.pearsonCorr.to_excel(self.dir_out_path + "\\CorrMatrix_" + self.out_name)