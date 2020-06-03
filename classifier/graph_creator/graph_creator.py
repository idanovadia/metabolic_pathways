import random
from queue import PriorityQueue
import pandas as pd
import numpy as np
import networkx as nx
import os
import json
from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import classifier.graph_creator.structural as structural
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
        self.labels_dir_path = self.getPath(self.config_parser.eval(self.__class__.__name__, "labels_dir_path"))
        self.sub2vecMethod = self.config_parser.eval(self.__class__.__name__, 'sub2vecMethod')
        self.threshold_weights = self.config_parser.eval(self.__class__.__name__, "threshold")
        self.main_graph_output_directory_path = self.getPath(
            self.config_parser.eval(self.__class__.__name__, "main_graph_output_directory"))
        self.sub_graphs_output_directory_path = self.getPath(
            self.config_parser.eval(self.__class__.__name__, "sub_graphs_output_directory"))
        self.subGraphs_list = []
        self.main_graph = nx.Graph()
        self.set_nodes = set()
        self.removeEdges = []
        self.adj_matrix_extensions = json.loads(self.config_parser.get(self.__class__.__name__, 'adj_matrix_extensions'))
        self.graph_extensions = self.config_parser.eval(self.__class__.__name__, "graph_extensions").split(",")


    def exec(self):
        if os.path.isdir(self.corr_matrix_path):#multiple matrices
            self.createMainGraph(type='multiple')
            self.run_adj_matrix_extensions()
            self.MultipleSubgraphs()
        else:
            self.createMainGraph(type='normal')
            self.run_adj_matrix_extensions()
            self.subGraphsCreator()
        if self.sub2vecMethod == 'structural':
            self.structural()
        self.writeMainGraph()
        self.run_graph_extensions()
        self.WriteAll()



    def run_adj_matrix_extensions(self):
        # add extensions here
        adj_extensions_dict = {}
        adj_extensions_dict['power_graph'] = self.powerGraph
        adj_extensions_dict['adj_matrix_power'] = self.setPowerAdjacencyMatrix
        adj_extensions_dict['adj_matrix_and_add'] = self.setAddPAMWithAM
        for extension , value in self.adj_matrix_extensions.items():
            if extension in adj_extensions_dict:
                adj_extensions_dict[extension](value)
                print(extension)

    def run_graph_extensions(self):
        graph_extensions_dict = {}
        graph_extensions_dict['add_neighbors_from_adj_matrix'] = self.addNeighborsToAllSubgraphs
        for extension in self.graph_extensions:
            if extension in graph_extensions_dict:
                graph_extensions_dict[extension]()
                print(extension)

    def structural(self):
        self.main_graph.remove_edges_from(self.main_graph.selfloop_edges())
        self.addToMainGraphDegree()
        self.subGraphs_list = structural.subGraphsCreator(self.subGraphs_list)

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

        def __init__(self, file_path, classify, type_graph, main_graph,nodes_list=None):
            self.file_path = file_path
            if nodes_list==None:
                self.nodes_list = self.createNodeList()
            else:
                self.nodes_list=nodes_list
            self.classify = classify
            self.type = type_graph
            self.graph = self.CreateSubGraph(main_graph)

        ''' csv file '''

        def createNodeList(self):
            csv_pd = pd.read_csv(self.file_path, index_col=0, header=0)
            l = [x.lower() for x in csv_pd.columns]
            return l

        '''generate sub graph and return it'''

        def CreateSubGraph(self, main_graph):
            subGraph = main_graph.subgraph(self.nodes_list).copy()
            if len(list(subGraph.nodes)) == 0:
                subGraph.add_nodes_from(self.nodes_list)
            subGraph.graph['label'] = self.classify
            subGraph.graph['type'] = self.type
            return subGraph

    # ''' main function '''

    # def create(self):
    #     self.createMainGraph()
    #
    #     # self.powerGraph()
    #     # self.setPowerAdjacencyMatrix()
    #     self.setAddPAMWithAM()
    #
    #     self.writeMainGraph()
    #     self.subGraphsCreator()
    #     # self.addRandomNeighbors()
    #     # self.NeighborsByPriority()
    #     self.WriteAll()
    #
    #     # nx.draw(self.main_graph,with_labels=True)
    #     # plt.savefig("filename.png")
    #     # self.plotGraph()

    ''' create list of sub graphs  '''

    def subGraphsCreator(self):
        list_of_dirs = os.listdir(self.labels_dir_path)
        for dirpath, dirnames, filenames in os.walk(self.labels_dir_path):
            if not dirnames:
                # for dir in list_of_dirs:
                #         dir_path = os.path.join(self.subGraphs_dir_path, dir)
                #         sub_graph_dir_list = os.listdir(dir_path)
                sub_graph_dir_list = os.listdir(dirpath)
                label = dirpath.split(sep=os.sep)[-1]
                type = dirpath.split(sep=os.sep)[-2]
                if label == "random":
                    label = "negative"
                for file in sub_graph_dir_list:
                    new_graph = self.sub_graph(os.path.join(dirpath, file), label, type, self.main_graph)
                    self.subGraphs_list.append(new_graph.graph)


    def MultipleSubgraphs(self):
        for sample_folder in os.listdir(self.labels_dir_path):
            for dirpath, dirnames, filenames in os.walk(self.labels_dir_path+os.sep+sample_folder):
                if not dirnames:
                    # for dir in list_of_dirs:
                    #         dir_path = os.path.join(self.subGraphs_dir_path, dir)
                    #         sub_graph_dir_list = os.listdir(dir_path)
                    sub_graph_dir_list = os.listdir(dirpath)
                    label = dirpath.split(sep=os.sep)[-1]
                    type = dirpath.split(sep=os.sep)[-2]
                    if label == "random":
                        label = "negative"
                    for file in sub_graph_dir_list:
                        new_graph = self.sub_graph(os.path.join(dirpath, file), label, type, self.main_graph,
                                                   nodes_list=self.getNodesTranslation(sample_name=sample_folder,reaction_file=os.path.join(dirpath, file)))
                        self.subGraphs_list.append(new_graph.graph)

    def getNodesTranslation(self,sample_name,reaction_file):
        csv_pd = pd.read_csv(reaction_file, index_col=0, header=0)
        l = [round(float(x)) for x in csv_pd.columns]
        return [self.subgraphs_translation[sample_name].get(str(key)) for key in l]
    def creteSetNodes(self):
        for list in self.subGraphs_list:
            for l in list.nodes_list:
                self.set_nodes.add(l)

    ''' create the main graph from correlation matrix '''

    def createMainGraph(self,type='multiple'):
        if type=='multiple':
            self.subgraphs_translation={}
            num=0
            for sample_folder in os.listdir(self.corr_matrix_path):
                for matrix in os.listdir(self.corr_matrix_path+os.sep+sample_folder):
                    self.subgraphs_translation[sample_folder]={}
                    if not matrix.startswith('~$') and matrix.endswith(".xlsx"):
                        num=self.multiple_graphCreator(self.corr_matrix_path+os.sep+sample_folder+os.sep+matrix,num)
        else: #single matrix
            self.graphCreator(self.corr_matrix_path)

    def multiple_graphCreator(self,file,num):
        folder_name=os.path.basename(os.path.abspath(os.path.join(file, os.pardir)))
        csv_pd = pd.read_excel(file, index_col=0, header=0)
        columns_headers = list(csv_pd)
        i, j = 0, 1
        for _, row in csv_pd.iterrows():
            # for i in range(j, len(row)):#adding nodes to graph and adding them as a number to the dictionary
                self.subgraphs_translation[folder_name][str(row.name).lower()]=num
                self.main_graph.add_node(num)
                num+=1
            # j += 1

        i, j = 0, 1
        for _, row in csv_pd.iterrows():
            for i in range(j, len(row)):  # adding edges
                # print("i : {} , j {} , row[i] {} , file {}".format(i,j,row[i],file))
                if abs(row[i]) >= float(self.threshold_weights):
                    self.main_graph.add_edge(u_of_edge=self.subgraphs_translation[folder_name][str(row.name).lower()],
                                             v_of_edge=self.subgraphs_translation[folder_name][str(columns_headers[i]).lower()],
                                             weight=row[i])
                elif self.subgraphs_translation[folder_name][str(columns_headers[i]).lower()] not in self.main_graph.nodes():
                    self.main_graph.add_node(self.subgraphs_translation[folder_name][str(columns_headers[i]).lower()])
            j += 1

        return num
    def graphCreator(self,file):
        csv_pd = pd.read_excel(file, index_col=0, header=0)
        columns_headers = list(csv_pd)
        i, j = 0, 1
        for _, row in csv_pd.iterrows():
            for i in range(j, len(row)):
                self.main_graph.add_node(str(row.name).lower())
                # print("i : {} , j {} , row[i] {} , file {}".format(i,j,row[i],file))
                if abs(row[i]) >= float(self.threshold_weights):
                    self.main_graph.add_edge(u_of_edge=str(row.name).lower(),
                                             v_of_edge=str(columns_headers[i]).lower(),
                                             weight=row[i])
                elif str(columns_headers[i]).lower() not in self.main_graph.nodes():
                    self.main_graph.add_node(str(columns_headers[i]).lower())
            j += 1


    # def generateWightsByThreshold(self):
    #     for (u, v, d) in self.main_graph.edges(data=True):
    #         if d['weight'] >= float(self.threshold_weights):
    #             d['weight'] = 1
    #         else:
    #             d['weight'] = 0
    #             self.removeEdges.append((u, v))
    #
    # ''' Remove edges from main graph that have weights = 0'''
    #
    # def removeEdgesByList(self):
    #     for i in range(len(self.removeEdges)):
    #         u = self.removeEdges[i][0]
    #         v = self.removeEdges[i][1]
    #         self.main_graph.remove_edge(u=u, v=v)

    # ############################################################################################################################################
    ''' Adding neighbors to each sub graph  '''

    def addNeighborsToAllSubgraphs(self):
        subgraphs_with_neighbors = []
        for i in self.subGraphs_list:
            subgraphs_with_neighbors.append(self.addAllNeighbors(i))
        self.subGraphs_list = subgraphs_with_neighbors

    ''' add neighbors to sub graph'''

    def addAllNeighbors(self, g_):
        new_g = g_.copy()
        self.number_of_neighbors = len(list(new_g.nodes))
        for node in list(new_g.nodes):
            neighbors = self.addNeighbors(g=new_g, node=node)
            if len(neighbors) == 0:
                break
            new_g = self.generateNewGraph(nodes=list(new_g.nodes), node=node)
        label = str(g_.graph['label'])
        type = str(g_.graph['type'])
        new_g.graph['label'] = label
        new_g.graph['type'] = type
        return new_g

    ''' create the new graph from main graph and the neighbors '''

    def generateNewGraph(self, nodes, node):
        nodes.append(node)
        return self.main_graph.subgraph(nodes).copy()

    ''' find all the neighbors in sub graph '''

    def addNeighbors(self, g, node):
        neighbors = set()
        neighbors.update(self.getNeighbors(node, self.main_graph))
        neighbors.difference_update(list(g.nodes))
        return neighbors

    ''' get neighbors of node '''

    def getNeighbors(self, node, _graph):
        return list(_graph.adj[node].keys())

    # ############################################################################################################################################

    ''' write all graphs to gml graph format'''

    def WriteAll(self):
        for id, graph in enumerate(self.subGraphs_list):
            self.writeFile(graph, id)

    ''' write a graph to gml graph format'''

    def writeFile(self, G, id):
        nx.write_gml(G=G, path=os.path.join(self.sub_graphs_output_directory_path, str(id) + ".gml"))

    ''' draw the main graph '''

    def writeMainGraph(self):
        nx.write_gml(G=self.main_graph, path=os.path.join(self.main_graph_output_directory_path, "main_graph.gml"))

    # ############################################################################################################################################

    # def plotGraph(self):
    #     elarge = [(u, v) for (u, v, d) in self.main_graph.edges(data=True) if d['weight'] > 0.5]
    #     esmall = [(u, v) for (u, v, d) in self.main_graph.edges(data=True) if d['weight'] <= 0.5]
    #     pos = nx.spring_layout(self.main_graph)  # positions for all nodes
    #     # nodes
    #     nx.draw_networkx_nodes(self.main_graph, pos, node_size=10)
    #     # edges
    #     nx.draw_networkx_edges(self.main_graph, pos, edgelist=elarge,
    #                            width=2)
    #     nx.draw_networkx_edges(self.main_graph, pos, edgelist=esmall,
    #                            width=2, alpha=0.5, edge_color='b', style='dashed')
    #     # labels
    #     nx.draw_networkx_labels(self.main_graph, pos, font_size=6, font_family='sans-serif')
    #     plt.axis('off')
    #     plt.show()
    # ############################################################################################################################################

    # --------------------------------------------------------------------------------------
    # power Graph- main
    def powerGraph(self, p):
        self.main_graph = nx.power(self.main_graph, p)

    #   return  AdjacencyMatrix power 2  - main
    def setPowerAdjacencyMatrix(self, p):
        nodes = self.main_graph.nodes
        self.main_graph = self.from_numpy_matrix(self.powerAdjacencyMatrix(p))
        self.main_graph = nx.relabel_nodes(self.main_graph, {i: j for i, j in enumerate(list(nodes))})


    # return AdjacencyMatrix power 2 + AdjacencyMatrix  - main
    def setAddPAMWithAM(self, p):
        nodes = self.main_graph.nodes
        self.main_graph = self.from_numpy_matrix(self.addPAMWithAM(p))
        self.main_graph = nx.relabel_nodes(self.main_graph, {i: j for i, j in enumerate(list(nodes))})

    # add AdjacencyMatrix power 2 + AdjacencyMatrix
    def addPAMWithAM(self, p):
        return self.powerAdjacencyMatrix(p) + self.to_numpy_matrix(self.main_graph)

    # convert AdjacencyMatrix to graph
    def from_numpy_matrix(self, matrix):
        return nx.from_numpy_matrix(matrix)

    # power AdjacencyMatrix
    def powerAdjacencyMatrix(self, p):
        return np.linalg.matrix_power(self.to_numpy_matrix(self.main_graph), p)

    # convert graph to AdjacencyMatrix
    def to_numpy_matrix(self, g):
        return nx.to_numpy_matrix(g, nodelist=g.nodes)

    # --------------------------------------------------------------------------------------
    def NeighborsByPriority(self):
        subgraphs_with_neighbors = []
        for i in self.subGraphs_list:
            subgraphs_with_neighbors.append(self.addNeighborsByPriority(i))
        self.subGraphs_list = subgraphs_with_neighbors

    def addNeighborsByPriority(self, g):
        new_g = g
        for count in range(self.number_of_neighbors):
            neighbors = self.addNeighbors_PriorityQueue(new_g)
            if len(neighbors.queue) == 0:
                break
            new_node = self.getNextNode(neighbors, new_g.nodes)
            new_g = self.generateNewGraph(list(new_g.nodes), new_node)
        return new_g

    def addNeighbors_PriorityQueue(self, g):
        neighbors = PriorityQueue()
        for vertex in g.nodes:
            for key, value in self.main_graph.adj._atlas[vertex].items():
                neighbors.put((-1 * value["weight"], key))
        return neighbors

    def getNextNode(self, neighbors, nodes):
        node = neighbors.queue[0]
        count = 1
        while node[1] in nodes:
            if len(neighbors.queue) == 0:
                return
            node = neighbors.queue[count]
            count += 1
        return node[0] * -1

    def addToMainGraphDegree(self):
        self.main_graph = structural.subGraphsCreator([self.main_graph])[0]





