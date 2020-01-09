import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import networkx as nx
import os
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
from configparser import ConfigParser
from distributed.worker import weight

''' Using to create the main graph from the correlation matrix and the sub graph lists  '''


class GraphCreator(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    '''
    corr_matrix_path - path to directory of corr matrix.
    subGraphs_dir_path - path to directory of label graphs.
    threshold_weights - make weight edge that  bigger or equal of threshold to 1 and less to 0.
    sub_graphs_output_directory_path - path to directory  to save the subgraphs with new weight.
    subGraphs_list - 
    main_graph - the complete graph.
    set_nodes
    removeEdges - edges that got weight 0 - to remove from main graph.
    '''
    def setup(self):
        self.corr_matrix_path = self.getPath(self.config_parser.eval(self.__class__.__name__, "corr_matrix_path"))
        self.subGraphs_dir_path = self.getPath(self.config_parser.eval(self.__class__.__name__, "subGraphs_dir_path"))
        self.threshold_weights = self.config_parser.eval(self.__class__.__name__, "threshold")
        self.sub_graphs_output_directory_path = self.getPath(self.config_parser.eval(self.__class__.__name__, "sub_graphs_output_directory"))
        self.subGraphs_list = []
        self.main_graph = nx.Graph()
        self.set_nodes = set()
        self.removeEdges = []

    def exec(self):
        self.create()

    '''
     Object of sub graph.  
    '''

    class sub_graph:
        '''
        file_path - path to label graph
        nodes_list - list of the nodes in the label graph
        classify - the class: positive/negative
        type - train/test sub graph
        graph - nx graph that has been created
        '''
        def __init__(self, file_path, classify, type_graph, main_graph):
            self.file_path = file_path
            self.nodes_list = self.createNodeList()
            self.classify = classify
            self.type = type_graph
            self.graph = self.getGraph(main_graph)


        ''' csv file '''

        def createNodeList(self):
            csv_pd = pd.read_csv(self.file_path, index_col=0, header=0)
            l = [x.lower() for x in csv_pd.columns]
            return l

        '''generate sub graph and return it'''
        def getGraph(self, main_graph):
            subGraph = main_graph.subgraph(self.nodes_list).copy()
            subGraph.graph['label'] = self.classify
            subGraph.graph['type'] = self.type
            return subGraph

    ''' main function '''

    def create(self):
        # self.creteSetNodes()
        self.createMainGraph()
        self.generateWightsByThreshold()
        self.removeEdgesByList()
        self.subGraphsCreator()
        self.WriteAll()
        # nx.draw(self.main_graph,with_labels=True)
        # plt.savefig("filename.png")
        # self.plotGraph()

    ''' create list of sub graphs  '''

    def subGraphsCreator(self):
        list_of_dirs = os.listdir(self.subGraphs_dir_path)
        for dirpath, dirnames, filenames in os.walk(self.subGraphs_dir_path):
            if not dirnames:
        # for dir in list_of_dirs:
        #         dir_path = os.path.join(self.subGraphs_dir_path, dir)
        #         sub_graph_dir_list = os.listdir(dir_path)
                sub_graph_dir_list = os.listdir(dirpath)
                label = dirpath.split(sep="\\")[-1]
                type = dirpath.split(sep="\\")[-2]
                for file in sub_graph_dir_list:
                    new_graph = self.sub_graph(os.path.join(dirpath, file), label, type, self.main_graph)
                    self.subGraphs_list.append(new_graph.graph)

    ''' create set on nodes from the lists of sub graphs '''

    def creteSetNodes(self):
        for list in self.subGraphs_list:
            for l in list.nodes_list:
                self.set_nodes.add(l)

    ''' create the main graph from correlation matrix '''

    def createMainGraph(self):
        csv_pd = pd.read_excel(self.corr_matrix_path, index_col=0, header=0)
        columns_headers = list(csv_pd)
        i, j = 0, 1
        for _, row in csv_pd.iterrows():
            for i in range(j, len(row)):
                self.main_graph.add_edge(u_of_edge=str(row.name).lower(), v_of_edge=str(columns_headers[i]).lower(), weight=row[i])
            j += 1

    '''
    Generate new weight 0 or 1 by threshold
    '''
    def generateWightsByThreshold(self):
        for (u, v, d) in self.main_graph.edges(data=True):
            if d['weight'] >= float(self.threshold_weights):
                d['weight'] = 1
            else:
                d['weight'] = 0
                self.removeEdges.append((u, v))

    ''' Remove edges from main graph that have weights = 0'''
    def removeEdgesByList(self):
        for i in range(len(self.removeEdges)):
            u = self.removeEdges[i][0]
            v = self.removeEdges[i][1]
            self.main_graph.remove_edge(u=u, v=v)

    ''' write all graphs to gml graph format'''
    def WriteAll(self):
        for id, graph in enumerate(self.subGraphs_list):
            self.writeFile(graph, id)

    ''' write a graph to gml graph format'''
    def writeFile(self, G, id):
        nx.write_gml(G=G, path=os.path.join(self.sub_graphs_output_directory_path, str(id) + ".gml"))

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


