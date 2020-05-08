import pickle
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import pandas as pd

class prediction(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.model_path= self.csv_output_directory = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, 'model_path'))
        self.x_test=self.csv_output_directory = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, 'x_test'))
        self.y_test = self.csv_output_directory = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, 'y_test'))

    def exec(self):
        self.load_model(input_path=self.model_path)
        self.predict()

    def load_model(self,input_path):
        f = open(input_path ,'rb')
        self.model = pickle.load(f)
        f.close()

    def predict(self):
        print(self.model.predict(pd.read_excel(self.x_test)))

