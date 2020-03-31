from classifier.Metrics.MetricsAbstract import MetricsAbstract
import numpy as np



class FN(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="FN"

    def calculate(self,y_pred,y_true):
        FN = 0

        y_true = np.array(y_true)
        for i in range(len(y_pred)):
            if y_pred[i] == 'negative' and y_true[i] != y_pred[i]:
                FN += 1
        return FN






