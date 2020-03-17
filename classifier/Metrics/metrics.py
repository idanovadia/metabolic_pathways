from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import json
from classifier.Metrics.Wrappers.accuracy_score import accuracyScoreWrapper
from classifier.Metrics.Wrappers.fscore import fscoreWrapper

class Metrics(AbstractConfigClass):

    def __init__(self):
        pass
    def setup(self):
        AbstractConfigClass.__init__(self)
        self.metrics_list = self.config_parser.eval(self.__class__.__name__, 'metrics_list').split(',')
        self.metrics_args = json.loads(self.config_parser.get(self.__class__.__name__, 'metrics_args'))
        self.metrics_dict={}
        self.metrics_dir = []


    def initMetricsDict(self):
        self.metrics_dict['accuracy']=accuracyScoreWrapper
        self.metrics_dict['f1score'] = fscoreWrapper


    def fillMetricsDir(self):
        for metric in self.metrics_list:
            self.metrics_dir.append(self.metrics_dict[metric](**self.metrics_args))

    def exec(self):
        self.initMetricsDict()
        self.fillMetricsDir()

