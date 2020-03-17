import lightgbm as lgb
from classifier.Classification.ClassifierAbstract import ClassifierAbstract
from sklearn.model_selection import GridSearchCV

class lightgbmWrapper(ClassifierAbstract):
    def __init__(self,**kwargs):
        self.name='lightgbm'
        self.learning_rate = kwargs['lgbm_lr']
        self.n_estimators = kwargs['lgbm_n_estimators']
        self.num_leaves = kwargs['lgbm_num_leaves']
        self.model = lgb.LGBMClassifier(learning_rate=float(self.learning_rate), metric='l1',
                                       n_estimators=int(self.n_estimators), num_leaves=int(self.num_leaves))



    def fit(self,x_train,y_train):
        self.model.fit(x_train, y_train,
                eval_metric=['auc', 'binary_logloss'],
                )
    def predict(self,x_test):
        return self.model.predict(x_test)
    def evaluate(self,x_test,y_test):
        return self.model.score(x_test,y_test)