from classifier import iniParams
from classifier.configuration.config_class import config_class
from classifier.graphPresentation.graphPresentation import GraphPresentation
from classifier.preprocessing.preprocessing import Preprocessing
from classifier.correlation_matrix_creator.correlation_matrix_creator import CorrMaxtrix
from classifier.graph_creator.graph_creator import GraphCreator
from classifier.sub2vec.sub2vec import Sub2Vec
from classifier.Classification.classification import classifier
from classifier.Plotter.Plotter import Plotter
import json
import sys

modules_dict = {}
modules_dict['Preprocessing'] = Preprocessing
modules_dict['CorrMaxtrix'] = CorrMaxtrix
modules_dict['GraphCreator'] = GraphCreator
modules_dict['Sub2Vec'] = Sub2Vec
modules_dict['classifier'] = classifier
# modules_dict['Plotter'] = Plotter

pipeline = []
config = config_class(sys.argv[1])
config = config.getConfig()

num_of_runs = int(config.get("DEFAULT", "num_of_runs"))

for module in config.sections():
    if modules_dict.get(module) and module != 'DEFAULT':
        pipeline.append(modules_dict.get(module)())


def config_params(class_name, param_name, val):
    # classification_args = json.loads(config.get(class_name, param_name))
    global config
    config.set(class_name, param_name, val)
    # config.set(class_name, param_name, json.dumps(classification_args))


def adj_matrix_extensions(class_name, param_name, val):
    for key_, value_ in val.items():
        # classification_args = json.loads(config.get(class_name, param_name))
        classification_args = {}
        classification_args[key_] = value_
        config.set(class_name, param_name, json.dumps(classification_args))


# example for changing random_forest_n_estimators value in each run by 100 until it reaches 500.
return_list = iniParams.return_list
for value in return_list:

    # GraphCreator
    config_params('GraphCreator', 'graph_extensions', value[2])
    config_params('GraphCreator', 'threshold', value[0])
    adj_matrix_extensions('GraphCreator', 'adj_matrix_extensions', value[1])
    # Sub2Vec
    config_params('Sub2Vec', 'random_walk_length', value[3])
    config_params('Sub2Vec', 'random_walk_number', value[4])
    classification_args = json.loads(config.get('Sub2Vec', 'doc2vec_args'))
    classification_args['vector_size'] = value[5].get("vector_size")
    classification_args['window_size'] = value[5].get("window_size")
    classification_args['learning_rate'] = value[5].get("learning_rate")
    classification_args['min_learning_rate'] = value[5].get("min_learning_rate")
    classification_args['min_count'] = value[5].get("min_count")
    classification_args['min_vocab_size'] = value[5].get("min_vocab_size")
    classification_args['workers'] = value[5].get("workers")
    classification_args['epochs'] = value[5].get("epochs")
    config.set('Sub2Vec', 'doc2vec_args', json.dumps(classification_args))
    config_params('Sub2Vec', 'rw_extensions', value[6])
    # classifier
    config_params('classifier', 'classifiers_list', value[7])
    classification_args = json.loads(config.get('classifier', 'classifiers_args'))
    classification_args['random_forest_max_depth'] = value[8].get("random_forest_max_depth")
    classification_args['random_forest_n_estimators'] = value[8].get("random_forest_n_estimators")
    classification_args['random_forest_min_samples_split'] = value[8].get("random_forest_min_samples_split")
    classification_args['random_forest_verbose'] = value[8].get("random_forest_verbose")
    classification_args['random_forest_random_state'] = value[8].get("random_forest_random_state")
    classification_args['random_forest_criterion'] = value[8].get("random_forest_criterion")
    classification_args['xgb_n_estimators'] = value[8].get("xgb_n_estimators")
    classification_args['xgb_objective'] = value[8].get("xgb_objective")
    classification_args['xgb_eval_metric'] = value[8].get("xgb_eval_metric")
    classification_args['xgb_verbose'] = value[8].get("xgb_verbose")
    classification_args['lgbm_lr'] = value[8].get("lgbm_lr")
    classification_args['lgbm_n_estimators'] = value[8].get("lgbm_n_estimators")
    classification_args['lgbm_num_leaves'] = value[8].get("lgbm_num_leaves")
    classification_args['cat_boost_iterations'] = value[8].get("cat_boost_iterations")
    classification_args['cat_boost_depth'] = value[8].get("cat_boost_depth")
    classification_args['cat_boost_learning_rate'] = value[8].get("cat_boost_learning_rate")
    classification_args['cat_boost_loss_function'] = value[8].get("cat_boost_loss_function")
    config.set('classifier', 'classifiers_args', json.dumps(classification_args))

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

    # for value in range(1):
    # classification_args=json.loads(config.get('classifier', 'classifiers_args'))
    # classification_args['random_forest_n_estimators']=value
    # config.set('classifier', 'classifiers_args',json.dumps(classification_args) )
    # for i in range(num_of_runs):
    #     print("run number {}".format(i))
    #     for element in pipeline:
    #         print("Initializing {}".format(element.__class__.__name__))
    #         element.setup()
    #
    #     print("\n")
    #
    #     for element in pipeline:
    #         print("Executing {}".format(element.__class__.__name__))
    #         element.exec()
    #         print("\n")

if __name__ == '__main__':
    pass
