import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

class CN_Cluster():
    def __init__(self, color,) -> None:
        self.order=None
        self.color = color

    def plot_corr(self,np_corr, size=10,title="", saving_path=""):
        df = pd.DataFrame(np_corr)
        # Compute the correlation matrix for the received dataframe
        X = df.corr().values
        d = sch.distance.pdist(X)  # vector of ('55' choose 2) pairwise distances
        L = sch.linkage(d, method='complete')
        ind = sch.fcluster(L, 0.5 * d.max(), 'distance')
        if self.order==None:
            self.order = [df.columns.tolist()[i] for i in list((np.argsort(ind)))]
        columns = self.order
        df = df.reindex(columns, axis=1)
        corr = df.corr()

        # Plot the correlation matrix
        plt.close()
        fig, ax = plt.subplots(figsize=(size, size))
        cax = ax.matshow(corr, cmap=self.color)
        plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
        plt.yticks(range(len(corr.columns)), corr.columns)

        # Add the colorbar legend
        cbar = fig.colorbar(cax, ticks=[-1, 0, 1], aspect=40, shrink=.8)
        plt.title(title)
        plt.savefig(saving_path)
        #plt.show()



