import pandas as pd
import numpy as np
from random import randint

from classifier.code_tools.Abstract_config_class import AbstractConfigClass


class Sub2Vec(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.randomWalk_threshold = self.config_parser.eval(self.__class__.__name__, 'random_walk_threshold')
        self.random_walk_graphs_to_create = self.config_parser.eval(self.__class__.__name__, 'random_walk_graphs_to_create')
        pass

    def exec(self):
        pass



