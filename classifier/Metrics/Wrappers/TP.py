from classifier.Metrics.MetricsAbstract import MetricsAbstract
import numpy as np



class TP(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="TP"

    def calculate(self,y_pred,y_true):
        TP = 0

        y_true=np.array(y_true)
        for i in range(len(y_pred)):
            if y_true[i] == y_pred[i] == 'positive':
                TP += 1
        return TP






