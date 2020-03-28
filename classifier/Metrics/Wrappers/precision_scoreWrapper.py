from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import precision_score



class precision_scoreWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="precision"

    def calculate(self,y_pred,y_true):
        return precision_score(y_true,y_pred,labels=['positive','negative'],average='binary',sample_weight=None,pos_label="positive")





