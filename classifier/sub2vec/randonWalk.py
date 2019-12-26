from random import randint


class RandomWalk():

    def __init__(self, threshold, number_of_graphs):
        self.threshold = threshold
        self.number_of_graphs = number_of_graphs

    def graphComparator(self, graph_1, graph_2):
        if list(graph_1.nodes).sort() == list(graph_2.nodes).sort():
            return True
        return False

    def insertGraphToSet(self, set_of_graphs, graph):
        if len(set_of_graphs != 0):
            for g in set_of_graphs:
                if self.graphComparator(g, graph):
                    return set_of_graphs
        set_of_graphs.add(graph)
        return set_of_graphs

    # Get sub-graph in nx format
    def randomWalk(self, sub_graph):
        self.empty_nodes_list = False
        rw_nodes_list = []
        count = 0
        threshold = self.randomWalk_threshold
        nodes = list(sub_graph.nodes)
        count, node = self.getNextNode(count, nodes, nodes, rw_nodes_list)
        while count < threshold and not self.empty_nodes_list:
            neighbors = self.getNeighbors(node, sub_graph)
            count, node = self.getNextNode(count, neighbors, nodes, rw_nodes_list)
        return rw_nodes_list

    def getNextNode(self, count, nodes, left_nodes, rw_nodes_list):
        node = self.randomNode(nodes, left_nodes)
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
