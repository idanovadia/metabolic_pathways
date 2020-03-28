from classifier.Metrics.MetricsAbstract import MetricsAbstract
from sklearn.metrics import precision_score



class precision_scoreWrapper(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="precision"

    def calculate(self,predictions):
        print("Calculating precision")
        return precision_score(predictions[0],predictions[1],labels=['positive','negative'],average='binary',sample_weight=None,pos_label="positive")





