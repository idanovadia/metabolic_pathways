Metabolites Pathway Classifier
=========================================

This project is a research expriment on metabolites pathway classification.
Given a labled data of metabolites pathway and a metabolic profile, we classify postivie and negative pathways by using graph embedding.



## Requirements
The project used the following versions for the packages. other versions needs to be test but should work fine
pandas 0.023
numpy  1.15.4 
networkx 2.3 
scikit-learn 0.21.3
gensim 3.80

## How to use

Run the run.py file with the config.ini (classifier/configuration/config.ini) file as an argument to the program.
Change the needed parameters in the config.ini file (listed below)

### Preprocessing
``input_file_path`` - the metabolic profile location

### CorrMaxtrix
``input_file_path`` - the metabolic profile location  after preprocessing 

### GraphCreator
``threshold`` - a number between 0 and 1 that decides the correlation threshold we should work with to build the graph 

``sub_graphs_output_directory`` - output path for gml files of subgraphs

``main_graph_output_directory`` = output path for gml file of the main graph

``number_Of_neighbors`` - number of neighbors to take incase we are using this option

``adj_matrix_extensions`` = {} an extensions for the adjacancy matrix as dictionary.they key is the extension name and the value is the value for the extension. ``{"power_graph" :2 , "adj_matrix_power":2 , "adj_matrix_and_add":2}``

``graph_extensions`` - a way to include more graph extensions - example while specifing the extension name in a list of seperated commas: "add_neighbors_from_adj_matrix"




### Sub2Vec
``random_walk_length``- number of steps from each node in a random walk

``random_walk_number`` - number of times random walk happens from each node

``sub2vecMethod`` - define neighborhood / structural

``subGraphs_directory_path`` - location of the subgraphs directory

``random_walk_directory_path_output`` - location of the random walk output as gml files for each random walk

``classifier_files_directory`` - supervised data location including 2 xlsx files for features and labels

``statistics_output_path`` - can provide a path that will save statistics of sub2vec

``main_graph_path`` - path of main graph

``doc2vec_args`` - a dictionary that holds hyperparameters for doc2vec as key and the value. example : ``{"vector_size": 10,"window_size": 3, "learning_rate": 0.025, "min_learning_rate": 0.0001,"min_count": 1, "min_vocab_size": "None" ,"workers": 4,"epochs": 50}``

``rw_extensions`` - extensions that can be done on random walks. expects a list of seperated commas example - ``"weighted_randomwalk", "rw_on_main_graph"``

``randomwalk_args`` args incase you are using weighted random walk : example  : ''{"weighted_next_node_multiplier":100}''

### Metrics
here you can define metrics or remove them for ignore. we support the following metrics ``"accuracy,precision,recall,f1score,TP,TN,FP,FN"``

define them with seperated commas in ``metrics_list``

you can also run extend it with arguments for the metrics with ''metrics_args''

### Classifier
you can choose from four different classifiers - ``RandomForest`` , ``SVM`` , ``CatBoost`` and ``lightGBM``. they can all run one after another so you can compare them later

define them in ``classifiers_list`` as a commas seperated

you can also pass arguments for each classifier (that we built as a wrapper to support our project better) by using ``classifiers_args``

* example : ``"random_forest_max_depth": 7,"random_forest_n_estimators": 500,
                 "random_forest_min_samples_split": 2, "random_forest_verbose": 0, "random_forest_random_state": "None",
                 "random_forest_criterion": "gini" , "xgb_n_estimators": 2, "xgb_objective": "binary:logistic" ,
                 "xgb_eval_metric" : "logloss" , "xgb_verbose": 1 , "lgbm_lr": 0.0125 , "lgbm_n_estimators": 200 ,"lgbm_num_leaves": 5,
                 "cat_boost_iterations" : 2 , "cat_boost_depth" : 2 , "cat_boost_learning_rate" : 0.5 , "cat_boost_loss_function" : "Logloss"}``


### Cleaner
run it if you would like to delete all the temperoray files after the end of the classifier run



