from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import json
from classifier.Validation.ValidationMethodAbstract import ValidationMethodAbstract
from classifier.Validation.Wrappers.LeaveOneOutWrapper import LeaveOneOutWrapper
from classifier.Validation.Wrappers.KFoldWrapper import KFoldWrapper

class Validation(AbstractConfigClass):

    def __init__(self,x_train,y_train):
        AbstractConfigClass.__init__(self)
        self.validation_list = self.config_parser.eval(self.__class__.__name__, 'validation_list').split(',')
        self.validation_args = json.loads(self.config_parser.get(self.__class__.__name__, 'validation_args'))
        self.validation_dict={}
        self.initValidationDict()
        self.val_dir = []
        self.fillValidationDirectory(x_train, y_train)
    def initValidationDict(self):
        self.validation_dict['LeaveOneOut']=LeaveOneOutWrapper
        self.validation_dict['KFold'] = KFoldWrapper


    def fillValidationDirectory(self,x_train,y_train):
        for validation in self.validation_list:
            self.val_dir.append(self.validation_dict[validation](x_train,y_train,**self.validation_args))






