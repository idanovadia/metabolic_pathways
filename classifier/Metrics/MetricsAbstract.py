

class MetricsAbstract():

    def __init__(self):
        pass
    def calculate(self,predictions):
        pass

    def getMetricName(self,train=False):
        if train:
            return "train " + self.name
        else:
            return "test " + self.name