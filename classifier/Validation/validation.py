from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import json
import pandas as pd
import sys
import inspect
from classifier.Validation.validationMethodAbstract import ValidationMethodAbstract
from classifier.Validation.Wrappers.LeaveOneOutWrapper import LeaveOneOutWrapper
from classifier.Validation.Wrappers.KFoldWrapper import KFoldWrapper

class validation(AbstractConfigClass):

    def __init__(self):
        pass
    def setup(self):
        AbstractConfigClass.__init__(self)
        self.validation_list = self.config_parser.eval(self.__class__.__name__, 'validation_list').split(',')
        self.validation_args = json.loads(self.config_parser.get(self.__class__.__name__, 'validation_args'))
        self.train_directory_path = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, "train_directory_path"))
        self.label_directory_path = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, "train_label_directory_path"))
        self.validation_dict={}
        self.val_dir = []


    def initValidationDict(self):
        self.validation_dict['LeaveOneOut']=LeaveOneOutWrapper
        self.validation_dict['KFold'] = KFoldWrapper


    def fillValidationDirectory(self,x_train,y_train):
        for validation in self.validation_list:
            self.val_dir.append(self.validation_dict[validation](x_train,y_train,**self.validation_args))


    def exec(self):
        self.x_train = pd.read_excel(self.train_directory_path)
        self.y_train = pd.read_excel(self.label_directory_path)[0]
        self.initValidationDict()
        self.fillValidationDirectory(self.x_train, self.y_train)

