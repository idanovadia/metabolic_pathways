from classifier.Classification.Wrappers import randomForestWrapper
from classifier.Classification.Wrappers import xgboostWrapper
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from classifier.Validation import validation
import json

class classifier(AbstractConfigClass):

    def __init__(self):
        pass

    def setup(self):
        self.classifiers_list = self.config_parser.eval(self.__class__.__name__, 'classifiers_list').split(',')
        self.classifiers_args = json.loads(self.config_parser.get(self.__class__.__name__, 'classifiers_args'))
        self.classifiers_dict = {}
        self.classifiers_dir = []
        self.valid=validation()
        self.valid.setup()




    def exec(self):
        self.valid.exec()

    def initClassifiersnDict(self):
        self.classifiers_dict['RandomForest']=randomForestWrapper
        self.classifiers_dict['xgboost'] = xgboostWrapper


    def fillClassifiersDirectory(self):
        for classifier in self.classifiers_list:
            self.val_dir.append(self.classifiers_dict[classifier](**self.classifiers_args))