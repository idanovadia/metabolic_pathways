from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import recall_score



class recal_scoreWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="recall"

    def calculate(self,predictions):
        print("calculating recall")
        return recall_score(predictions[0],predictions[1],average='binary',sample_weight=None,pos_label="positive")





