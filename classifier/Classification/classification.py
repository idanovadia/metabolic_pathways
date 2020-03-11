from classifier.Classification.Wrappers.randomForestWrapper import RandomForestWrapper
from classifier.Classification.Wrappers.xgboostWrapper import xgboostWrapper
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
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




    def exec(self):
        self.valid.exec()
        self.classify()


    def initClassifiersnDict(self):
        self.classifiers_dict['RandomForest']=RandomForestWrapper
        self.classifiers_dict['xgboost'] = xgboostWrapper


    def fillClassifiersDirectory(self):
        for classifier in self.classifiers_list:
            self.classifiers_dir.append(self.classifiers_dict[classifier](**self.classifiers_args))


    def classify(self):
        validations= getattr(self.valid,'val_dir')
        for val in validations :
            val_gen=val.split()
            for x_train , y_train , x_test , y_test in val_gen:
                for cls in self.classifiers_dir:
                    cls.fit(x_train,y_train)
                    # print(cls.predict(x_test))
                    print(cls.evaluate(x_test,y_test))