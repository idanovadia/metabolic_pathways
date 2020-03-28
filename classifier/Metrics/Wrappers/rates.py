from classifier.Metrics.MetricsAbstract import MetricsAbstract
import numpy as np



class rates(MetricsAbstract):
    def __init__(self,**kwargs):
        self.name="rates"

    def calculate(self,y_pred,y_true):
        TP = 0
        FP = 0
        TN = 0
        FN = 0

        y_true=np.array(y_true)
        for i in range(len(y_pred)):
            if y_true[i] == y_pred[i] == 'positive':
                TP += 1
            if y_pred[i] == 'positive' and y_true[i] != y_pred[i]:
                FP += 1
            if y_true[i] == y_pred[i] == 'negative':
                TN += 1
            if y_pred[i] == 'negative' and y_true[i] != y_pred[i]:
                FN += 1

        print("TP {} FP {} TN {} FN {}".format(TP,FP,TN,FN))

        return 1

        # return recall_score(y_true,y_pred,labels=['positive','negative'],average='binary',sample_weight=None,pos_label="positive")





