import pandas as pd


class Result():

    def __init__(self,cls,val,scores):
        self.classifier=cls
        self.validation=val
        self.scores=scores


    def getPandas(self,df,**kwargs):
        correlation_tresh=kwargs['correlation_treshold']
        randomwalk_tresh=kwargs['random_walk_treshold']
        df=df.append(pd.Series([correlation_tresh,
                                randomwalk_tresh,
                                self.classifier,
                                self.validation,
                                self.scores['train']['accuracy'],
                                self.scores['train']['f1 score'],
                                self.scores['train']['precision'],
                                self.scores['train']['recall'],
                                self.scores['train']['FP'],
                                self.scores['train']['FN'],
                                self.scores['train']['TP'],
                                self.scores['train']['TN'],
                                self.scores['test']['accuracy'],
                                self.scores['test']['f1 score'],
                                self.scores['test']['precision'],
                                self.scores['test']['recall'],
                                self.scores['test']['FP'],
                                self.scores['test']['FN'],
                                self.scores['test']['TP'],
                                self.scores['test']['TN']
                                ], index=df.columns ),ignore_index=True)
        # ['classifier', 'validation', 'train accuracy', 'train F1',
        #        'train Precision', 'train Recall', 'train FP', ' train FN', 'train TP',
        #        'train TN', 'test accuracy', 'test F1', 'test Precision', 'test Recall',
        #        'test FP', ' test FN', 'test TP', 'test TN'],
        return df