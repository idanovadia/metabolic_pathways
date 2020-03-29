from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import accuracy_score


class accuracyScoreWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="accuracy"
        pass
    def calculate(self,y_pred,y_true):
        return accuracy_score(y_true,y_pred,sample_weight=None,)


