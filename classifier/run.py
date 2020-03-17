from classifier.Classification.classification import classifier
from classifier.configuration.config_class import getConfig
from classifier.graphPresentation.graphPresentation import GraphPresentation
from classifier.preprocessing.preprocessing import Preprocessing
from classifier.correlation_matrix_creator.correlation_matrix_creator import CorrMaxtrix
from classifier.graph_creator.graph_creator import GraphCreator
from classifier.sub2vec.sub2vec import Sub2Vec

modules_dict = {}
modules_dict['Preprocessing'] = Preprocessing
modules_dict['CorrMaxtrix'] = CorrMaxtrix
modules_dict['GraphCreator'] = GraphCreator
modules_dict['Sub2Vec'] = Sub2Vec
modules_dict['classifier'] = classifier

pipeline = []

for module in getConfig().sections():
    if modules_dict.get(module):
        pipeline.append(modules_dict.get(module)())

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
