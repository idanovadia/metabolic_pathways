from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import json
from classifier.Metrics.Wrappers.accuracy_score import accuracyScoreWrapper
from classifier.Metrics.Wrappers.fscore import fscoreWrapper
from classifier.Metrics.Wrappers.recall_scoreWrapper import recal_scoreWrapper
from classifier.Metrics.Wrappers.precision_scoreWrapper import precision_scoreWrapper
from classifier.Metrics.Wrappers.rates import rates


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
        self.metrics_dict['recall']=recal_scoreWrapper
        self.metrics_dict['precision']=precision_scoreWrapper
        self.metrics_dict['rates']=rates


    def fillMetricsDir(self):
        for metric in self.metrics_list:
            self.metrics_dir.append(self.metrics_dict[metric](**self.metrics_args))

    def exec(self):
        self.initMetricsDict()
        self.fillMetricsDir()

