from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import accuracy_score


class accuracyScoreWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="accuracy"
        pass
    def calculate(self,predictions):
        return accuracy_score(predictions[0],predictions[1],sample_weight=None,)


