from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from .Wrappers.LeaveOneOutWrapper import LeaveOneOutWrapper
from .Wrappers.KFoldWrapper import KFoldWrapper

class ValidationFactory(AbstractConfigClass):

    def __init__(self,x_train,y_train):
        self.kfold_splits=self.getPath(
                relative_path=self.config_parser.eval(self.__class__.__name__, 'kfold_splits'))
        self.val_dir = []
        self.fillValidationDirectory(x_train, y_train)


    def fillValidationDirectory(self,x_train,y_train):
        self.val_dir = []
        self.val_dir.append(LeaveOneOutWrapper(x_train,y_train))
        self.val_dir.append(KFoldWrapper(x_train,y_train,kfold_split= self.kfold_splits))