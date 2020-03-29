from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import recall_score



class recal_scoreWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="recall"

    def calculate(self,y_pred,y_true):
        return recall_score(y_true,y_pred,labels=['positive','negative'],average='binary',sample_weight=None,pos_label="positive")





