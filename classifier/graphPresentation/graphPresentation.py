from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import networkx as nx
import os
import matplotlib.pyplot as plt


class GraphPresentation(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.graphs_dir_path = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, "graphs_dir_path"))
        self.graphs_dir__output_path = self.getPath(
            relative_path=self.config_parser.eval(self.__class__.__name__, "graphs_dir__output_path"))
        self.graphs = []

    def exec(self):
        self.readGraphs()
        self.draw()

    def readGraphs(self):
        for filename in os.listdir(self.graphs_dir_path):
            try:
                self.graphs.append((filename, (nx.read_gml(os.path.join(self.graphs_dir_path, filename)))))
            except:
                print(filename)
                continue

    def draw(self):
        for i in self.graphs:
            name = i[0]
            graph = i[1]
            fig = plt.figure(figsize=(60, 60))
            pos = nx.spring_layout(graph, k=0.15, iterations=10)
            nx.draw_networkx(graph, pos=pos, node_color='#A0CBE2', node_size=200, font_size=30,
                             edge_color='#BB0000',
                             with_labels=True)
            plt.axis('equal')
            plt.show()
            fig.savefig(os.path.join(self.graphs_dir__output_path, name + ".pdf"))
