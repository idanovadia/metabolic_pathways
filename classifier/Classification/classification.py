from classifier.Classification.Wrappers.randomForestWrapper import RandomForestWrapper
from classifier.Classification.Wrappers.xgboostWrapper import xgboostWrapper
from classifier.Classification.Wrappers.lightgbmWrapper import lightgbmWrapper
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from classifier.Classification.result import Result
from classifier.Metrics.metrics import Metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from classifier.Validation.validation import validation
import json
import pandas as pd

class classifier(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.classifiers_list = self.config_parser.eval(self.__class__.__name__, 'classifiers_list').split(',')
        self.classifiers_args = json.loads(self.config_parser.get(self.__class__.__name__, 'classifiers_args'))
        self.classifiers_dict = {}
        self.classifiers_dir = []
        self.valid=validation()
        self.metrics=Metrics()
        self.valid.setup()
        self.metrics.setup()
        self.initClassifiersnDict()
        self.fillClassifiersDirectory()
        self.resultdict=[]




    def exec(self):
        self.valid.exec()
        self.metrics.exec()
        self.classify()
        self.printdict()
        self.outputResult()


    def initClassifiersnDict(self):
        self.classifiers_dict['RandomForest']=RandomForestWrapper
        self.classifiers_dict['xgboost'] = xgboostWrapper
        self.classifiers_dict['lightgbm'] =lightgbmWrapper


    def fillClassifiersDirectory(self):
        for classifier in self.classifiers_list:
            self.classifiers_dir.append(self.classifiers_dict[classifier](**self.classifiers_args))


    def classify(self):
        validations= getattr(self.valid,'val_dir')

        for val in validations :
            for cls in self.classifiers_dir:
                val_gen = val.split()
                predictions=[]
                for x_train , y_train , x_test , y_test in val_gen:
                    cls.fit(x_train, y_train)
                    # print(cls.predict(x_test))
                    # print("Train Score : {} , Test Score : {} ".format(cls.evaluate(x_train, y_train),
                    #
                    #
                    predictions.append([cls.predict(x_train), y_train,cls.predict(x_test),y_test])

                print((cls.name,val.name))
                scores=self.calculateScore(predictions)
                self.resultdict.append(Result(cls.name,val.name,scores))
                # self.resultdict[(cls.name,val.name)]={'train':trainsum/count,'test':testsum/count}
        self.printdict()




    def printdict(self):
        print(self.resultdict)

    def calculateScore(self,predictions):
        result={"train":[] , "test":[]}


        for metric in self.metrics.metrics_dir:
            count=0
            test_sum=0
            train_sum=0
            for pred in predictions:
                train_sum+=metric.calculate([pred[0],pred[1]])
                test_sum+=metric.calculate([pred[2],pred[3]])
                count+=1
            train_score=(metric.getMetricName(train=True),train_sum/count)
            test_score=(metric.getMetricName(),test_sum/count)

            result['train'].append(train_score)
            result['test'].append(test_score)

        return result

    def outputResult(self):
        df = pd.DataFrame(columns=['classifier', 'validation', 'train'])
        df=df.T
        i=44


