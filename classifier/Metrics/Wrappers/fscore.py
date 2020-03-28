from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import f1_score
import numpy as np



class fscoreWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="f1 score"
        pass
    def calculate(self,y_pred,y_true):
        return f1_score(y_true,y_pred,average='binary',labels=np.unique(y_pred),sample_weight=None,pos_label="positive")





