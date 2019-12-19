import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import networkx as nx
import os

from distributed.worker import weight

''' Using to create the main graph from the correlation matrix and the sub graph lists  '''


class graph_creator:

    def __init__(self, subGraphs_dir_path=None, corr_matrix_path=None):
        self.corr_matrix_path = corr_matrix_path
        self.subGraphs_dir_path = subGraphs_dir_path
        self.subGraphs_list = []
        self.main_graph = nx.Graph()
        self.set_nodes = set()

    '''
     Object of sub graph.  
    '''

    class sub_graph:

        def __init__(self, file_path, classify):
            self.file_path = file_path
            self.nodes_list = self.createNodeList()
            self.classify = classify

        ''' csv file '''
        def createNodeList(self):
            csv_pd = pd.read_csv(self.file_path, index_col=0, header=0)
            return list(csv_pd.columns)

    ''' main function '''
    def create(self):
        self.subGraphsCreator()
        # self.creteSetNodes()
        self.createMainGraph()
        # nx.draw(self.main_graph,with_labels=True)
        # plt.savefig("filename.png")
        # self.plotGraph()

    ''' create list of sub graphs  '''
    def subGraphsCreator(self):
        list_of_dirs = os.listdir(self.subGraphs_dir_path)
        for dir in list_of_dirs:
            dir_path = os.path.join(self.subGraphs_dir_path, dir)
            sub_graph_dir_list = os.listdir(dir_path)
            for file in sub_graph_dir_list:
                self.subGraphs_list.append(self.sub_graph(os.path.join(dir_path, file), dir))

    ''' create set on nodes from the lists of sub graphs '''
    def creteSetNodes(self):
        for list in self.subGraphs_list:
            for l in list.nodes_list:
                self.set_nodes.add(l)

    ''' create the main graph from correlation matrix '''
    def createMainGraph(self):
        csv_pd = pd.read_excel(self.corr_matrix_path, index_col=0, header=0)
        columns_headers = list(csv_pd)
        i, j = 0, 0
        for _, row in csv_pd.iterrows():
            for i in range(j, len(row)):
                self.main_graph.add_edge(u_of_edge=row.name, v_of_edge=columns_headers[i], weight=row[i])
            j += 1

    ''' draw the main graph '''
    def plotGraph(self):
        elarge = [(u, v) for (u, v, d) in self.main_graph.edges(data=True) if d['weight'] > 0.5]
        esmall = [(u, v) for (u, v, d) in self.main_graph.edges(data=True) if d['weight'] <= 0.5]
        pos = nx.spring_layout(self.main_graph)  # positions for all nodes
        # nodes
        nx.draw_networkx_nodes(self.main_graph, pos, node_size=10)
        # edges
        nx.draw_networkx_edges(self.main_graph, pos, edgelist=elarge,
                               width=2)
        nx.draw_networkx_edges(self.main_graph, pos, edgelist=esmall,
                               width=2, alpha=0.5, edge_color='b', style='dashed')
        # labels
        nx.draw_networkx_labels(self.main_graph, pos, font_size=6, font_family='sans-serif')
        plt.axis('off')
        plt.show()
