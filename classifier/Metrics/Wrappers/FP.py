from classifier.Metrics.MetricsAbstract import MetricsAbstract
import numpy as np



class FP(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="FP"

    def calculate(self,y_pred,y_true):
        FP = 0

        y_true = np.array(y_true)
        for i in range(len(y_pred)):
            if y_pred[i] == 'positive' and y_true[i] != y_pred[i]:
                FP += 1
        return FP






