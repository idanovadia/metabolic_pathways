from random import randint
import networkx as nx
import random


class RandomWalk():

    def __init__(self, threshold, number_of_graphs,args,extensions):
        self.threshold = threshold
        self.number_of_graphs = number_of_graphs
        self.args=args
        self.extensions=extensions


    # def graphComparator(self, graph_1, graph_2):
    #     if sorted(list(graph_1.nodes)) == sorted(list(graph_2.nodes)):
    #         return True
    #     return False

    def insertGraphToSet(self, list_of_graphs, graph):
        rwList = []
        for counter, j in enumerate(graph.nodes):
            for i in range(self.number_of_graphs):
                if 'rw_on_main_graph' in self.extensions:
                    new_graph=self.randomWalk_on_main_graph()
                new_graph = self.randomWalk(graph, j, i)
                new_graph.graph["name"] = str(i) + "_" + str(counter) + "_" + new_graph.graph["name"]
                rwList.append(new_graph)
        list_of_graphs.append(rwList)
        return list_of_graphs
    def randomWalk_on_main_graph(self,main_graph,root):
        self.empty_nodes_list = False
        rw_nodes_list = []
        count = 0
        nodes=list(main_graph.node(root))
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
            if 'weighted_randomwalk' in self.extensions:

                count, node = self.getNextNodeByWeights(count, nodes, rw_nodes_list, sub_graph, node)
            else:
                count, node = self.getNextNode(count, nodes, rw_nodes_list)

        # sub_graph.graph["name"] = str(sub_name) + "_" + sub_graph.graph["name"]
        return sub_graph.subgraph(rw_nodes_list).copy()



    def getNextNodeByWeights(self, count, nodes, rw_nodes_list, sub_graph, node):
        sum_of_weights = self.getSumOfWeights(sub_graph, node)
        random_number = randint(0, sum_of_weights)
        new_node = random.choice(nodes)
        multiplier=self.args['weigted_next_node_multiplier']
        counter_of_weights = round(sub_graph[node]._atlas[new_node]['weight'] * multiplier)
        while random_number > counter_of_weights:
            nodes.remove(new_node)
            new_node = random.choice(nodes)
            counter_of_weights += round(sub_graph[node]._atlas[new_node]['weight'] * multiplier)
        count += 1
        return count, new_node


    def getSumOfWeights(self, sub_graph, node):
        sum_of_weights = 0
        a_dict = sub_graph._adj.get(node)
        for key, value in a_dict.items():
            sum_of_weights += round(value['weight'] * 100)
        return sum_of_weights


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
