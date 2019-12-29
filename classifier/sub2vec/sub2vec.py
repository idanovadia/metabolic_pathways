import pandas as pd
import numpy as np
from random import randint
import networkx as nx
import os
import classifier.sub2vec.randonWalk as rw
from classifier.code_tools.Abstract_config_class import AbstractConfigClass


class Sub2Vec(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    '''
    randomWalk_threshold - number of nodes in each graph
    random_walk_graphs_to_create - number of graphs to create of each sub graph
    subGraphs_directory_path - directory path to sub graphs files (networks format)
    '''
    def setup(self):
        self.randomWalk_threshold = self.config_parser.eval(self.__class__.__name__, 'random_walk_threshold')
        self.random_walk_graphs_to_create = self.config_parser.eval(self.__class__.__name__, 'random_walk_graphs_to_create')
        self.subGraphs_directory_path = self.getPath(relative_path=self.config_parser.eval(self.__class__.__name__, 'subGraphs_directory_path'))
        self.subGraphs_list = []
        self.list_of_graphs = []
        pass

    def exec(self):
        self.generateSubGraphs()
        random_walk_object = rw.RandomWalk(threshold=self.randomWalk_threshold, number_of_graphs=self.random_walk_graphs_to_create)
        for g in self.subGraphs_list:
            for i in range(self.random_walk_graphs_to_create):
                self.list_of_graphs = random_walk_object.insertGraphToSet(list_of_graphs=self.list_of_graphs, graph=random_walk_object.randomWalk(g))

    # use directory path and read all the saved sab graphs there
    def generateSubGraphs(self):
        for filename in os.listdir(self.subGraphs_directory_path):
            self.subGraphs_list.append(nx.read_gml(os.path.join(self.subGraphs_directory_path,filename)))


