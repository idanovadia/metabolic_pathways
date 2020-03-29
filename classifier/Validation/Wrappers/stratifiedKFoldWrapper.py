from sklearn.model_selection import StratifiedKFold
from classifier.Validation.validationMethodAbstract import ValidationMethodAbstract


class stratifiedKFoldWrapper(ValidationMethodAbstract):

    def __init__(self,x_train,y_train,**kwargs):
        self.x_train=x_train
        self.y_train=y_train
        self.splits=kwargs['stratifiedkfold_split']
        self.name='StratifiedKFold'


    def split(self):
        kf= StratifiedKFold(self.splits, shuffle=True)
        for train_index, test_index in kf.split(self.x_train,self.y_train):
            x_train, x_test = self.x_train.iloc[train_index], self.x_train.iloc[test_index]
            y_train, y_test = self.y_train.iloc[train_index], self.y_train.iloc[test_index]
            yield x_train , y_train , x_test ,y_test











