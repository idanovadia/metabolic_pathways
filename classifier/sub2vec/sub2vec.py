import pandas as pd
import numpy as np
from random import randint
import networks as nx
import os

from classifier.code_tools.Abstract_config_class import AbstractConfigClass


class Sub2Vec(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.randomWalk_threshold = self.config_parser.eval(self.__class__.__name__, 'random_walk_threshold')
        self.random_walk_graphs_to_create = self.config_parser.eval(self.__class__.__name__, 'random_walk_graphs_to_create')
        self.subGraphs_directory_path = self.getPath(relative_path=self.config_parser.eval(self.__class__.__name__, 'subGraphs_directory_path'))
        self.subGraphs_list = []
        pass

    def exec(self):
        pass

    # use directory path and read all the saved sab graphs there
    def generateSubGraphs(self):
        for filename in os.listdir(self.subGraphs_directory_path):
            self.subGraphs_list.append(nx.read_gml(os.path.join(self.subGraphs_directory_path,filename)))


