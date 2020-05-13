
from classifier.configuration.config_class import config_class
from classifier.graphPresentation.graphPresentation import GraphPresentation
from classifier.preprocessing.preprocessing import Preprocessing
from classifier.correlation_matrix_creator.correlation_matrix_creator import CorrMaxtrix
from classifier.graph_creator.graph_creator import GraphCreator
from classifier.sub2vec.sub2vec import Sub2Vec
from classifier.Classification.classification import classifier
from classifier.Plotter.Plotter import Plotter
import sys

modules_dict = {}
modules_dict['Preprocessing'] = Preprocessing
modules_dict['CorrMaxtrix'] = CorrMaxtrix
modules_dict['GraphCreator'] = GraphCreator
modules_dict['Sub2Vec'] = Sub2Vec
modules_dict['classifier'] = classifier
# modules_dict['Plotter'] = Plotter

pipeline = []
config=config_class(sys.argv[1])
config=config.getConfig()

num_of_runs = int(config.get("DEFAULT", "num_of_runs"))


for module in config.sections():
    if modules_dict.get(module) and module!='DEFAULT':
        pipeline.append(modules_dict.get(module)())

#running test x times
for i in range(num_of_runs):
    print("run number {}".format(i))
    for element in pipeline:
        print("Initializing {}".format(element.__class__.__name__))
        element.setup()

    print("\n")

    for element in pipeline:
        print("Executing {}".format(element.__class__.__name__))
        element.exec()
        print("\n")

if __name__ == '__main__':
    pass
