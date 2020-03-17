import xgboost as xgb
from classifier.Classification.ClassifierAbstract import ClassifierAbstract

class xgboostWrapper(ClassifierAbstract):
    def __init__(self,**kwargs):
        self.n_estimators = kwargs['xgb_n_estimators']
        self.objective= kwargs['xgb_objective']
        self.eval_metric=kwargs['xgb_eval_metric']
        self.verbose=kwargs['xgb_verbose']
        self.model=xgb.XGBModel(n_estimators=self.n_estimators,objective=self.objective)

    def fit(self,x_train,y_train):
        self.model.fit(x_train,y_train,eval_metric=self.eval_metric,verbose=self.verbose)
    def predict(self,x_test):
        return self.model.predict(x_test)
    def evaluate(self,x_test,y_test):
        return self.model.evaluate(x_test,y_test)





param_dist = {'objective':'binary:logistic', 'n_estimators':2}

