

class MetricsAbstract():

    def __init__(self):
        pass
    def calculate(self,y_pred,y_true):
        pass

    def getMetricName(self,train=False):
        # if train:
        #     return "train " + self.name
        # else:
        #     return "test " + self.name
        return self.name