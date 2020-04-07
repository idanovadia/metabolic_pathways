from random import randint
import networkx as nx
import random


class RandomWalk():

    def __init__(self, threshold, number_of_graphs):
        self.threshold = threshold
        self.number_of_graphs = number_of_graphs

    # def graphComparator(self, graph_1, graph_2):
    #     if sorted(list(graph_1.nodes)) == sorted(list(graph_2.nodes)):
    #         return True
    #     return False

    def insertGraphToSet(self, list_of_graphs, graph):
        rwList = []
        for counter, j in enumerate(graph.nodes):
            for i in range(self.number_of_graphs):
                new_graph = self.randomWalk(graph, j, i)
                new_graph.graph["name"] = str(i) + "_" + str(counter) + "_" + new_graph.graph["name"]
                rwList.append(new_graph)
        list_of_graphs.append(rwList)
        return list_of_graphs

    # Get sub-graph in nx format
    def randomWalk(self, sub_graph, root, sub_name):
        self.empty_nodes_list = False
        rw_nodes_list = []
        count = 0
        threshold = self.threshold
        nodes = list(sub_graph.nodes)
        count, node = self.getFirstNode(count, nodes, rw_nodes_list, root)
        while count < threshold and len(nodes) > 0:
            nodes = self.getNeighbors(node, sub_graph)
            if len(nodes) == 0:
                break
            count, node = self.getNextNode(count, nodes, rw_nodes_list)
        # sub_graph.graph["name"] = str(sub_name) + "_" + sub_graph.graph["name"]
        return sub_graph.subgraph(rw_nodes_list).copy()

    def getFirstNode(self, count, nodes, rw_nodes_list, root):
        rw_nodes_list.append(root)
        nodes.remove(root)
        count += 1
        return count, root

    def getNextNode(self, count, nodes, rw_nodes_list):
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
