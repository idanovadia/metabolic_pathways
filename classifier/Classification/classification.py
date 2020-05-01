from classifier.Classification.Wrappers.catboostWrapper import CatBoost
from classifier.Classification.Wrappers.randomForestWrapper import RandomForestWrapper
from classifier.Classification.Wrappers.svmWrapper import SvmWrapper
from classifier.Classification.Wrappers.xgboostWrapper import xgboostWrapper
from classifier.Classification.Wrappers.lightgbmWrapper import lightgbmWrapper
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from classifier.Classification.result import Result
from classifier.Metrics.metrics import Metrics
import timeit
from classifier.Validation.validation import validation
import json
import os
import pandas as pd


class classifier(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.csv_output_directory = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, 'csv_output_directory'))
        self.output_file_name = self.config_parser.eval(self.__class__.__name__, "output_file_name")
        self.classifiers_list = self.config_parser.eval(self.__class__.__name__, 'classifiers_list').split(',')
        self.classifiers_args = json.loads(self.config_parser.get(self.__class__.__name__, 'classifiers_args'))
        self.classifiers_dict = {}
        self.classifiers_dir = []
        self.valid = validation()
        self.metrics = Metrics()
        self.valid.setup()
        self.metrics.setup()
        self.initClassifiersnDict()
        self.fillClassifiersDirectory()
        self.resultdict = []
        self.result_dataframe=pd.DataFrame()
        self.train_size=0
        self.test_size=0

    def exec(self):
        self.valid.exec()
        self.metrics.exec()
        self.classify()
        self.outputResult()

    def initClassifiersnDict(self):
        self.classifiers_dict['RandomForest'] = RandomForestWrapper
        self.classifiers_dict['xgboost'] = xgboostWrapper
        self.classifiers_dict['lightgbm'] = lightgbmWrapper
        self.classifiers_dict['CatBoost'] = CatBoost
        self.classifiers_dict['Svm'] = SvmWrapper

    def fillClassifiersDirectory(self):
        for classifier in self.classifiers_list:
            self.classifiers_dir.append(self.classifiers_dict[classifier](**self.classifiers_args))

    def classify(self):
        validations = getattr(self.valid, 'val_dir')

        for val in validations:
            for cls in self.classifiers_dir:
                val_gen = val.split()
                predictions = []
                for x_train, y_train, x_test, y_test in val_gen:
                    cls.fit(x_train, y_train)
                    predictions.append([cls.predict(x_train), y_train, cls.predict(x_test), y_test])
                    self.train_size+=len(x_train)
                    self.test_size += len(x_test)

                scores = self.calculateScore(predictions,train_size=self.train_size,test_size=self.test_size)
                self.resultdict.append(Result(cls.name, val.name, scores))
                self.train_size=0
                self.test_size=0

    def printdict(self):
        print(self.resultdict)

    def calculateScore(self, predictions,train_size,test_size):
        result = {"train": {}, "test": {},"train size":0,"test_size":0}
        result["train size"]=train_size
        result["test size"] = test_size
        for metric in self.metrics.metrics_dir:
            count = 0
            test_sum = 0
            train_sum = 0
            for pred in predictions:
                train_sum += metric.calculate(pred[0], pred[1])
                test_sum += metric.calculate(pred[2], pred[3])
                count += 1
            if metric.getMetricName() not in ['TP','TN','FP','FN']:
                train_score =  (train_sum / count)
                test_score = (test_sum / count)
            else:
                train_score =  (train_sum / count)
                test_score = test_sum

            result['train'][metric.getMetricName()]=train_score
            result['test'][metric.getMetricName()]=test_score

        return result

    def outputResult(self):
        columns = ['Correlation threshold','RW Length','RW num of times','Classifier', 'Validation','Improvements', 'train accuracy', 'train F1 score','train Precision','train Recall','train FP', ' train FN','train TP','train TN','test accuracy', 'test F1 score','test Precision','test Recall','test FP', ' test FN','test TP','test TN','train size','test size','embedding size','doc2vec hyperparameters']
        added_cols = {'correlation_treshold':self.config_parser.eval('GraphCreator', "threshold"),
                      'random_walk_length':self.config_parser.eval('Sub2Vec', 'random_walk_length'),
                      'random walk num of times':self.config_parser.eval('Sub2Vec', 'random_walk_number'),
                      'improvements':self.getImprovments(),
                      'embedding_size':json.loads(self.config_parser.get('Sub2Vec', 'doc2vec_args'))['vector_size'],
                      'doc2vec hyper parameters':json.loads(self.config_parser.get('Sub2Vec', 'doc2vec_args'))}
        if added_cols['improvements']=="":
            added_cols['improvements']="None"
        if os.path.exists(self.csv_output_directory+os.sep+self.output_file_name+'.xlsx'):
            self.result_dataframe=pd.read_excel(self.csv_output_directory+os.sep+self.output_file_name+'.xlsx')
        else :
            self.result_dataframe=pd.DataFrame(columns=columns)

        for result in self.resultdict:
            self.result_dataframe = result.getPandas(self.result_dataframe,**added_cols)

        self.result_dataframe.to_excel(self.csv_output_directory + "/" + self.output_file_name+".xlsx",index=False)

    def getImprovments(self):
        extensions=[str(self.config_parser.eval('GraphCreator', 'adj_matrix_extensions')).replace('}','').replace('{','').replace(':','=').replace("'", ""),
                    self.config_parser.eval('GraphCreator','graph_extensions'),
                    str(self.config_parser.eval('Sub2Vec', 'rw_extensions'))
                    ]
        last=""
        result=""
        for extension in extensions:
            if last=="":
                result+=extension
            else:
                result+=','+extension
            last=extension
        return result