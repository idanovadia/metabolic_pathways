from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import f1_score


class fscoreWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="f1 score"
        pass
    def calculate(self,predictions):
        return f1_score(predictions[0],predictions[1],average='binary',sample_weight=None,pos_label="positive")





