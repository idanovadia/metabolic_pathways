from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import os
import re




class Plotter(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)



    def setup(self):
        self.data=json.loads(self.config_parser.get(self.__class__.__name__, 'data'))
        self.present=json.loads(self.config_parser.get(self.__class__.__name__, 'presentation'))
        self.show_params=self.config_parser.get(self.__class__.__name__, 'show_params')



    def exec(self):
        for inv in self.present:
            for data in self.data:
                type=self.present[inv]['type']
                classes=self.getclasses(self.data[data]['file'],self.present[inv]['groupby'])
                values=self.getMeanperClass(self.data[data]['file'],self.present[inv]['groupby'],self.present[inv]['compare_columns'])
                if type=='group_bar':
                    self.group_bar(classes,values,self.present[inv]['title'],self.present[inv]['compare_columns'])


    def generateData(self):
        pass

    def getclasses(self,data,column):
        df=pd.read_excel(self.getPath(data))

        return [x for x in df[column].unique()]

    def getMeanperClass(self,data,groupby,columns):
        df = pd.read_excel(self.getPath(data))
        cols=columns.split(',')

        return [(df.groupby(groupby)[cols[0]].agg(lambda x: x.unique().mean()).values) , (df.groupby(groupby)[cols[1]].agg(lambda x: x.unique().mean()).values)]

    def group_bar(self,classes,values,title,labels,width=0.35,):
        values1 , values2=values[0] , values[1]
        label1 , label2 = labels.split(',')[0],labels.split(',')[1]

        x = np.arange(len(classes))  # the label locations


        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, values1, width, label=label1)
        rects2 = ax.bar(x + width / 2, values2, width, label=label2)
        rects=[rects1,rects2]
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(x)
        ax.set_xticklabels(classes)
        ax.legend()
        for rect in rects:
            for bar in rect:
                height = bar.get_height()
                ax.annotate('{}'.format(height),
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        fig.tight_layout()

        plt.show()

        i=5
        pass



    def autolabel(self,rects,ax):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
        return ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')






    #for on data
    #open excel
    #read columns to present
    #read compare columns
    #read show params
    #plot