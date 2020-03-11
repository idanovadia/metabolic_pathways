from sklearn.model_selection import LeaveOneOut
from ..ValidationMethodAbstract import ValidationMethodAbstract


class LeaveOneOutWrapper(ValidationMethodAbstract):

    def __init__(self,x_train,y_train,**kwargs):
        self.x_train=x_train
        self.y_train=y_train
        self.name='Leave One Out'

    def split(self):
        loo = LeaveOneOut()
        loo.get_n_splits(self.x_train)
        for train_index, test_index in loo.split(self.data):
            x_train, x_test = self.x_train.iloc[train_index, :], self.x_train.iloc[test_index, :]
            y_train, y_test = self.y_train[train_index], self.y_train[test_index]
            yield  x_train , y_train , x_test , y_test











