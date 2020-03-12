from classifier.Classification.Wrappers.randomForestWrapper import RandomForestWrapper
from classifier.Classification.Wrappers.xgboostWrapper import xgboostWrapper
from classifier.Classification.Wrappers.lightgbmWrapper import lightgbmWrapper
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from classifier.Validation.validation import validation
import json

class classifier(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.classifiers_list = self.config_parser.eval(self.__class__.__name__, 'classifiers_list').split(',')
        self.classifiers_args = json.loads(self.config_parser.get(self.__class__.__name__, 'classifiers_args'))
        self.classifiers_dict = {}
        self.classifiers_dir = []
        self.valid=validation()
        self.valid.setup()
        self.initClassifiersnDict()
        self.fillClassifiersDirectory()
        self.resultdict={}




    def exec(self):
        self.valid.exec()
        self.classify()
        self.printdict()


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
                trainsum = 0
                testsum = 0
                count = 0
                for x_train , y_train , x_test , y_test in val_gen:
                    cls.fit(x_train, y_train)
                    # print(cls.predict(x_test))
                    # print("Train Score : {} , Test Score : {} ".format(cls.evaluate(x_train, y_train),
                    #                                                    cls.evaluate(x_test, y_test)))
                    count += 1
                    trainsum += cls.evaluate(x_train, y_train)
                    testsum += cls.evaluate(x_test, y_test)
                print((cls.name,val.name,count))
                self.resultdict[(cls.name,val.name)]={'train':trainsum/count,'test':testsum/count}




    def printdict(self):
        print(self.resultdict)

    def calculateScore(self):
        f1_score()
        accuracy_score()
