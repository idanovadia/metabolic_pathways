from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np


class mseWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="mse"
        pass
    def calculate(self,predictions):
        le = LabelEncoder()
        le.fit(['negative', 'positive'])
        preds=le.transform(predictions[0])
        preds_true = le.transform(predictions[1])
        # enc = OneHotEncoder(handle_unknown='ignore')
        # enc.fit([['negative', 0], ['positive', 1]])
        # enc.get_feature_names(['negative', 'positive'])
        return mean_squared_error(preds,preds_true)


