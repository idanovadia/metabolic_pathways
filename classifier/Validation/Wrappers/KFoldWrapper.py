from sklearn.model_selection import KFold
from ..validationMethodAbstract import ValidationMethodAbstract


class KFoldWrapper(ValidationMethodAbstract):

    def __init__(self,x_train,y_train,**kwargs):
        self.x_train=x_train
        self.y_train=y_train
        self.splits=kwargs['kfold_split']
        self.name='KFold'


    def split(self):
        kf= KFold(self.splits, shuffle=True)
        for train_index, test_index in kf.split(self.x_train):
            x_train, x_test = self.x_train[train_index], self.x_train[test_index]
            y_train, y_test = self.y_train[train_index], self.y_train[test_index]
            yield x_train , y_train , x_test ,y_test











