from classifier.Metrics.MetricsAbstract import MetricsAbstract
import numpy as np



class TN(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="TN"

    def calculate(self,y_pred,y_true):
        TN = 0

        y_true = np.array(y_true)
        for i in range(len(y_pred)):
            if y_true[i] == y_pred[i] == 'negative':
                TN += 1
        return TN

