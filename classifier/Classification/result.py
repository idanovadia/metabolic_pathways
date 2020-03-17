import pandas as pd

class Result():

    def __init__(self,cls,val,scores):
        self.classifier=cls
        self.validation=val
        self.scores=scores


    def getPandas(self,df):
        df=df.append(pd.Series([self.classifier,self.validation,self.scores['train'],self.scores['test']], index=df.columns ),ignore_index=True)
        return df