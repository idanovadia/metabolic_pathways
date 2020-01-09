from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from keras.utils import to_categorical
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import networkx as nx
import os


class Classifier(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.train_directory_path = self.getPath(relative_path=self.config_parser.eval(self.__class__.__name__, "train_directory_path"))
        self.train_label_directory_path = self.getPath(relative_path=self.config_parser.eval(self.__class__.__name__, "train_label_directory_path"))
    def exec(self):
        self.model()


    def model(self):
        self.train = pd.read_excel(self.train_directory_path)
        self.label = pd.read_excel(self.label_directory_path)[0]
        X_train, X_test, y_train, y_test = train_test_split(self.train, self.label, test_size=0.3, random_state = 42)

        Random_Forest = RandomForestClassifier(n_estimators=30, max_depth=2, random_state=0)
        Random_Forest.fit(X_train, y_train)
        y_pred = Random_Forest.predict(X_test)
        print("Accuracy:", metrics.accuracy_score(y_test, y_pred))