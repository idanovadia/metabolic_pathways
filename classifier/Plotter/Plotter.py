from pandas.util.testing import getPeriodData

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
        self.data = json.loads(self.config_parser.get(self.__class__.__name__, 'data'))
        self.present = json.loads(self.config_parser.get(self.__class__.__name__, 'presentation'))
        self.show_params = self.config_parser.get(self.__class__.__name__, 'show_params')

    def exec(self):
        for inv in self.present:
            data = self.data[self.present[inv]['data']]['file']
            type = self.present[inv]['type']
            classes = self.getclasses(data, self.present[inv]['groupby'])
            values = self.getMeanperClass(data, self.present[inv]['groupby'], self.present[inv]['compare_columns'])
            if type == 'group_bar':
                self.group_bar(classes, values, self.present[inv]['title'], self.present[inv]['compare_columns'],
                               self.present[inv]['ylabel'])
            elif type == 'line':
                self.line(classes, values, self.present[inv]['title'], self.present[inv]['labels'],
                          self.present[inv]['ylabel'], self.present[inv]['xlabel'])
            elif type == 'errorBar':
                self.error_bar(classes, data, self.present[inv]['title'], self.present[inv]['compare_columns'],
                               self.present[inv]['ylabel'], self.present[inv]['xlabel'],
                               int(self.present[inv]['numberOfSamples']))
            elif type == 'roc':
                self.roc(classes, data, self.present[inv]['title'], self.present[inv]['compare_columns'],
                         self.present[inv]['ylabel'], self.present[inv]['xlabel'],
                         int(self.present[inv]['numberOfSamples']))

    # Correlation
    # threshold, test
    # FP, test
    # FN, test
    # TP, test
    # TN
    def roc(self, classes, data, title, labels, ylabel, xlabel, number_of_samples):
        df = self.getDate(data)
        labels = str(labels).split(",");
        # df = df[labels]
        for c in classes:
            for t in (df[labels[0]].unique().round(1)):
                new_df = df[df[labels[0]].round(1) == t]
                self.create_roc(new_df, labels, c,ylabel,xlabel,title+" - correlation threshold: "+str(t))

    def create_roc(self, new_df, labels, class_,ylabel,xlabel,title):
        import sklearn.metrics as metrics
        fpr, tpr = [0], [0]
        new_df = new_df[new_df['Improvements'] == class_][labels]
        for index, row in new_df.iterrows():
            fpr.append(self.fpr(fp=row["test FP"],tn=row["test TN"]))
            tpr.append(self.fpr(fp=row["test TP"],tn=row[" test FN"]))
        fpr.append(1)
        tpr.append(1)
        fpr.sort()
        tpr.sort()
        plt.plot([0, 1], [0, 1],fpr, tpr)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.title(title)
        plt.plot([0, 1], [0, 1], 'r--')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        # plt.scatter(fpr, tpr)
        plt.show()

    def fpr(self, fp, tn):
        return fp / (fp + tn)

    def tpr(self, tp, fn):
        return tp / (tp + fn)

    def getDate(self, data):
        return pd.read_excel(self.getPath(data))

    def error_bar(self, classes, data, title, labels, ylabel, xlabel, number_of_samples):
        df = self.getDate(data)
        for c in classes:
            new_title = title + "\n" + c
            x_test, y_test, xerr_test, yerr_test = self.getLabelsArrays(df, c, str(labels).split(",")[0],
                                                                        str(labels).split(",")[1], number_of_samples)
            x_train, y_train, xerr_train, yerr_train = self.getLabelsArrays(df, c, str(labels).split(",")[0],
                                                                            str(labels).split(",")[2],
                                                                            number_of_samples)
            self.create_error_bar(x_test=x_test, y_test=y_test, xerr_test=xerr_test, yerr_test=yerr_test,
                                  x_train=x_train, y_train=y_train, xerr_train=xerr_train, yerr_train=yerr_train,
                                  xlabel=xlabel, ylabel=ylabel, title=new_title)

    def getLabelsArrays(self, df, class_name, label_x, label_y, number_of_samples):
        x, y, xerr, yerr = [], [], [], []
        data_x = df[df['Improvements'] == class_name][label_x]
        data_y = df[df['Improvements'] == class_name][label_y]
        for i in range(0, len(data_x), number_of_samples - 1):
            tmp_x = data_x[i:i + number_of_samples - 1]
            tmp_y = data_y[i:i + number_of_samples - 1]
            x, xerr = self.error_bar_params(tmp_x, x, xerr)
            y, yerr = self.error_bar_params(tmp_y, y, yerr)
        return x, y, xerr, yerr

    def error_bar_params(self, values, points, errors_rate):
        points.append(values.mean())
        errors_rate.append((values.max() - values.min()) / 2)
        return points, errors_rate

    def create_error_bar(self, x_test, y_test, xerr_test, yerr_test, x_train,
                         y_train, xerr_train, yerr_train, xlabel, ylabel, title):
        fig, ax = plt.subplots()
        ax.errorbar(x_test, y_test,
                    xerr=xerr_test,
                    yerr=yerr_test,
                    fmt='o',
                    ecolor='r')
        ax.errorbar(x_train, y_train,
                    xerr=xerr_train,
                    yerr=yerr_train,
                    fmt='o',
                    ecolor='m')

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        plt.gca().legend(('Test', 'Train'))
        # plt.legend(loc="upper left")
        # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax.set_yticks(np.arange(0.65, 0.9, step=0.05))
        name = str(title).split('\n')[0] + "-" + str(title).split('\n')[1]
        plt.savefig(self.getPath('classifier/data/Graphs_images') + "\\" + name + '.png')
        plt.show()

    def generateData(self):
        pass

    def getclasses(self, data, column):
        df = pd.read_excel(self.getPath(data))

        return [x for x in df[column].unique()]

    def getMeanperClass(self, data, groupby, columns):
        df = pd.read_excel(self.getPath(data))
        cols = columns.split(',')

        return [df.groupby(groupby)[x].agg(lambda x: x.unique().mean()).values for x in cols]

    def group_bar(self, classes, values, title, labels, ylabel, width=0.35):
        values1, values2 = values[0], values[1]
        label1, label2 = labels.split(',')[0], labels.split(',')[1]

        x = np.arange(len(classes))

        fig, ax = plt.subplots(figsize=(15, 12))
        rects1 = ax.bar(x - width / 2, values1, width, label=label1)
        rects2 = ax.bar(x + width / 2, values2, width, label=label2)
        rects = [rects1, rects2]
        ax.set_yticks(np.arange(0, 1, step=0.3))
        plt.ylim(0, 1)
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
                            ha='center', va='bottom', )

        # txt = '\n'+'\n'+'\n'+'\n'+"I need the caption to be present a little below X-axis"
        # plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)
        fig.tight_layout()

        plt.show()

    def line(self, classes, values, title, labels, ylabel, xlabel):
        labels = labels.split(",")

        for i in range(len(labels)):
            x = [x for x in classes]
            y = [y for y in values[i]]
            x.reverse()
            plt.plot(x, y, label=labels[i])

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.title(title)

        plt.legend()

        plt.show()

    def autolabel(self, rects, ax):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
        return ax.annotate('{}'.format(height),
                           xy=(rect.get_x() + rect.get_width() / 2, height),
                           xytext=(0, 3),  # 3 points vertical offset
                           textcoords="offset points",
                           ha='center', va='bottom')

    # for on data
    # open excel
    # read columns to present
    # read compare columns
    # read show params
    # plot
