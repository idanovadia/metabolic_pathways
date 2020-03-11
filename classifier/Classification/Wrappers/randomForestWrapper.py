from sklearn.ensemble import RandomForestClassifier
from classifier.Classification.ClassifierAbstract import ClassifierAbstract

class RandomForestWrapper(ClassifierAbstract):
    def __init__(self,**kwargs):
        self.n_estimators = kwargs['random_forest_n_estimators']
        self.criterion= kwargs['random_forest_criterion']
        self.min_samples_split=kwargs['random_forest_min_samples_split']
        self.verbose=kwargs['random_forest_verbose']
        self.max_depth=['random_forest_max_depth']
        self.random_state=['random_forest_random_state']
        self.model=RandomForestClassifier(max_depth=50,
                                          verbose=int(self.verbose),
                                          min_samples_split=int(self.min_samples_split),
                                          criterion=self.criterion,
                                          n_estimators=int(self.n_estimators))

        pass
    def fit(self,x_train,y_train):
        self.model.fit(x_train,y_train)
    def predict(self,x_test):
        return self.model.predict(x_test)
    def evaluate(self,x_test,y_test):
        return self.model.score(x_test,y_test)