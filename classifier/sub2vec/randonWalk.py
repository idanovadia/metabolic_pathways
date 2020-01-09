from random import randint
import networkx as nx
import random


class RandomWalk():

    def __init__(self, threshold, number_of_graphs):
        self.threshold = threshold
        self.number_of_graphs = number_of_graphs

    def graphComparator(self, graph_1, graph_2):
        if sorted(list(graph_1.nodes)) == sorted(list(graph_2.nodes)):
            return True
        return False

    def insertGraphToSet(self, list_of_graphs, graph):
        # if len(list_of_graphs) != 0:
        #     for g in list_of_graphs:
        #         if self.graphComparator(g, graph):
        #             return list_of_graphs
        list_of_graphs.append(graph)
        return list_of_graphs

    # Get sub-graph in nx format
    def randomWalk(self, sub_graph):
        self.empty_nodes_list = False
        rw_nodes_list = []
        count = 0
        threshold = self.threshold
        nodes = list(sub_graph.nodes)
        count, node = self.getNextNode(count, nodes, rw_nodes_list)
        while count < threshold and len(nodes) > 0:
            nodes = self.getNeighbors(node, sub_graph)
            if len(nodes) == 0:
                break
            count, node = self.getNextNode(count, nodes, rw_nodes_list)
        return sub_graph.subgraph(rw_nodes_list)

    def getNextNode(self, count, nodes, rw_nodes_list):
        # node = self.randomNode(nodes, left_nodes)
        node = random.choice(nodes)
        rw_nodes_list.append(node)
        nodes.remove(node)
        count += 1
        return count, node

    def getNeighbors(self, node, sub_graph):
        return list(sub_graph.adj[node].keys())

    def randomNode(self, nodes_list, left_nodes):
        index = randint(0, len(nodes_list) - 1)
        while nodes_list[index] not in left_nodes:
            nodes_list.remove(nodes_list[index])
            if len(nodes_list) == 0:
                self.empty_nodes_list = True
            else:
                index = randint(0, len(nodes_list) - 1)
        return nodes_list[index]
