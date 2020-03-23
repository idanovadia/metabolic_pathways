# pip install catboost
# pip install ipywidgets

from catboost import CatBoostClassifier, Pool

from classifier.Classification.ClassifierAbstract import ClassifierAbstract


class CatBoost(ClassifierAbstract):
    def __init__(self, **kwargs):
        self.iterations = kwargs['cat_boost_iterations']
        self.depth = kwargs['cat_boost_depth']
        self.learning_rate = kwargs['cat_boost_learning_rate']
        self.loss_function = kwargs['cat_boost_loss_function']
        self.name = 'CatBoost'
        self.model = model = CatBoostClassifier(iterations=self.iterations,
                                                depth=self.depth,
                                                learning_rate=self.learning_rate,
                                                loss_function=self.loss_function,
                                                verbose=True)

        pass

    def fit(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def predict(self, x_test):
        return self.model.predict(x_test)

    def evaluate(self, x_test, y_test):
        return self.model.score(x_test, y_test)
