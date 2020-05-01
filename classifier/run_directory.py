
from classifier.configuration.config_class import config_class
from classifier.graphPresentation.graphPresentation import GraphPresentation
from classifier.preprocessing.preprocessing import Preprocessing
from classifier.correlation_matrix_creator.correlation_matrix_creator import CorrMaxtrix
from classifier.graph_creator.graph_creator import GraphCreator
from classifier.sub2vec.sub2vec import Sub2Vec
from classifier.Classification.classification import classifier
from classifier.Plotter.Plotter import Plotter
import os
import sys

modules_dict = {}
modules_dict['Preprocessing'] = Preprocessing
modules_dict['CorrMaxtrix'] = CorrMaxtrix
modules_dict['GraphCreator'] = GraphCreator
modules_dict['Sub2Vec'] = Sub2Vec
modules_dict['classifier'] = classifier
modules_dict['Plotter'] = Plotter

pipeline = []



# add config files from directory
config_files=[]
for filename in os.listdir(sys.argv[1]):
    if filename.endswith(".ini"):
         config_files.append(sys.argv[1]+os.sep+filename)

for config_file in config_files:
    config=config_class(config_file)
    config=config.getConfig()
    print("__________________________________")
    print("running {}".format(config_file))
    print("__________________________________")
    for module in config.sections():
        if modules_dict.get(module) and module != 'DEFAULT':
            pipeline.append(modules_dict.get(module)())
    #running test x times
    num_of_runs = int(config.get("DEFAULT", "num_of_runs"))
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
    pipeline.clear()

if __name__ == '__main__':
    pass
