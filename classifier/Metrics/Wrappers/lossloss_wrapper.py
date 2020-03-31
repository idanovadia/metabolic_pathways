from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import log_loss


class loglossWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="logloss"
        pass
    def calculate(self,y_pred,y_true):
        return log_loss(y_true,y_pred)


