from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import os
import re
import math




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
                    self.group_bar(classes,values,self.present[inv]['title'],self.present[inv]['compare_columns'],self.present[inv]['ylabel'])


    def generateData(self):
        pass

    def getclasses(self,data,column):
        df=pd.read_excel(self.getPath(data))

        return [x for x in df[column].unique()]

    def getMeanperClass(self,data,groupby,columns):
        df = pd.read_excel(self.getPath(data))
        cols=columns.split(',')

        return [df.groupby(groupby)[x].agg(lambda x: x.unique().mean()).values for x in cols]

    def group_bar(self,classes,values,title,labels,ylabel,width=0.3):
        values1, values2 = values[0], values[1]
        label1, label2 = labels.split(',')[0], labels.split(',')[1]

        x = np.arange(len(classes))

        fig, ax = plt.subplots(figsize=(10, 10))
        rects1 = ax.bar(x - width / 2, values1, width, label=label1)
        rects2 = ax.bar(x + width / 2, values2, width, label=label2)
        rects = [rects1, rects2]
        ax.set_yticks(np.arange(min(values1.min(),values2.min())-min(values1.min(),values2.min())/2,max(values1.max(),values2.max()+0.7), step=0.1))
        ax.set_ylabel(ylabel)
        ax.set_title(title)
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

        # txt = '\n'+'\n'+'\n'+'\n'+"I need the caption to be present a little below X-axis"
        # plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)
        fig.tight_layout()

        plt.show()


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