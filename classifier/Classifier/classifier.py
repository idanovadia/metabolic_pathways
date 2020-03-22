from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import LeaveOneOut
from sklearn import metrics
import timeit
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import networkx as nx
import os


class Classifier(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)


    def setup(self):
        self.csv_output_directory = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, 'csv_output_directory'))
        self.train_directory_path = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, "train_directory_path"))
        self.output_file_name = self.config_parser.eval(self.__class__.__name__, "output_file_name")
        self.label_directory_path = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, "train_label_directory_path"))
        self.df_results = pd.DataFrame(columns=["Id", "Classifier", "Validation", "Result", "Runtime"])
        self.data = pd.read_excel(self.train_directory_path)
        self.label = pd.read_excel(self.label_directory_path)[0]
        self.id_counter = 1

    def exec(self):
        self.LeaveOneOut()
        self.saveFile()
        self.printResults()

    def LeaveOneOut(self, ):
        begin_run = timeit.timeit()
        sum = 0
        count = 0

        loo = LeaveOneOut()
        loo.get_n_splits(self.data)
        for train_index, test_index in loo.split(self.data):
            X_train, X_test = self.data.iloc[train_index, :], self.data.iloc[test_index, :]
            y_train, y_test = self.label[train_index], self.label[test_index]
            # X_train, X_test, y_train, y_test = train_test_split(self.train, self.label, test_size=0.3, random_state = 42)

            Random_Forest = RandomForestClassifier(n_estimators=30, max_depth=2, random_state=0)
            Random_Forest.fit(X_train, y_train)
            y_pred = Random_Forest.predict(X_test)
            count += 1
            sum += metrics.accuracy_score(y_test, y_pred)
            # print("Accuracy: {}".format(sum))
        print(sum / count)
        time_run = timeit.timeit() - begin_run
        self.appendToDfResults(Random_Forest.__class__.__name__, loo.__class__.__name__, sum / count, time_run)

    def appendToDfResults(self, classifier, validation_method, result, runtime):
        self.df_results.loc[self.id_counter] = [self.id_counter]+[classifier]+[validation_method]+[result]+[runtime]

    def saveFile(self):
        self.df_results.to_excel(self.csv_output_directory+"/"+self.output_file_name+"_"+str(timeit.timeit())+".xlsx")

    def printResults(self):
        print(self.df_results.to_string())


