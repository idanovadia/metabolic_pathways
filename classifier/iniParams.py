import itertools
import numpy

# GraphCreator

# GraphCreator_threshold = ["0.6"]
# GraphCreator_adj_matrix_extensions = [{"":""}]
# GraphCreator_graph_extensions = ["''"]
GraphCreator_threshold = [str(x) for x in numpy.arange(0.2, 1, 0.1)]
GraphCreator_adj_matrix_extensions = [{"": ""}, {"adj_matrix_and_add": 2}, {"power_graph": 2},
                                      {"adj_matrix_and_add": 2}]
GraphCreator_graph_extensions = ["''", "'add_neighbors_from_adj_matrix'"]

# Sub2Vec

Sub2Vec_random_walk_length = ["30"]
# Sub2Vec_random_walk_length = ["1", "5", "10", "15", "20", "25", "30"]
Sub2Vec_random_walk_number = ["5"]
Sub2Vec_doc2vec_args = [
    {"vector_size": 10, "window_size": 2, "learning_rate": 0.025, "min_learning_rate": 0.0001, "min_count": 1,
     "min_vocab_size": "None", "workers": 4, "epochs": 50}
]
Sub2Vec_rw_extensions = ["''", "'weigted_randomwalk'", "'rw_on_main_graph'"]

# Classifier

Classifier_classifiers_list = ["'RandomForest'"]
Classifier_classifiers_args = [
    {"random_forest_max_depth": 4, "random_forest_n_estimators": 50,
     "random_forest_min_samples_split": 2, "random_forest_verbose": 0, "random_forest_random_state": "None",
     "random_forest_criterion": "gini", "xgb_n_estimators": 2, "xgb_objective": "binary:logistic",
     "xgb_eval_metric": "logloss", "xgb_verbose": 1, "lgbm_lr": 0.0125, "lgbm_n_estimators": 200, "lgbm_num_leaves": 5,
     "cat_boost_iterations": 2, "cat_boost_depth": 2, "cat_boost_learning_rate": 0.5,
     "cat_boost_loss_function": "Logloss"}

]

main_list = [GraphCreator_threshold, GraphCreator_adj_matrix_extensions, GraphCreator_graph_extensions,
             Sub2Vec_random_walk_length, Sub2Vec_random_walk_number, Sub2Vec_doc2vec_args,
             Sub2Vec_rw_extensions, Classifier_classifiers_list, Classifier_classifiers_args]

return_list = list(itertools.product(*main_list))

# Classifier_classifiers_args = [
#     [
#         ["2", "4"], ["100", "200", "300", "400", "500"], ["2"], ["0"], ["None"], ["gini"], ["2"], ["logistic"],
#         ["logloss"], ["1"], ['0.0125'], ["200"], ["5"], ["2"], ["2"], ["0.5"], ["Logloss"]
#     ]
#
# ]
