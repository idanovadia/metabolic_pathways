# The Simulator #
The purpose of the Simulator is to simulate data for the classifier. The Simulator passes on to the Classifier the following data: correlation matrices, positive reactions and negative reactions

## Requirements ##
To use this project you will need a Python run-time environment.
Packges used and version:

|Package | Version |
| ------ | ------ |
| torch | 1.0.1 |
| networkx | 2.2 | 
| matplotlib | 3.0.3 |
| openpyxl | 2.6.1 |
| unicodecsv | 0.14.1 |
| xlrd | 1.2.0 |

Also, please notice that in order to use the GPU file, you must have GPU card on your computer

## How to use ##

**Training the Simulator:**

There are 2 options to train the Simulator
1. Running the Reaction_NN_Matrix
2. Ruunig the Reaction_NN_Matrix_gpu

Training the Reaction_NN_Matrix:
    1. Running the Simulator with fake data should be activated by running the following line: 
        test = Test()
        test.run_tests(False)
        You can find the results in the "Results" folder - the file results.xlsx contains the main results
    
        You can play with the following parameter:
        m_count = number of metabolties in profile
        reactions_count = number of reactions in model
        dataset_size = number of fake matrcies to create
        minibatch_size = number of random initial substrates
        epochs = number of epchos
        iterations = number of times to activate different reactions on the metabolic profile (random number between 0 to itreations)
    
    
    2. Running the Simulator with real data should be activayed by running the following line:
        test = Test()
        test.run_tests(True)
        You can find the results in the "Results" folder - the file results.xlsx contains the main results.
        The real matrix should be located in the "Original Files" folder, or rather change the path under the "Matrix Reader" class

Training the Reaction_NN_Matrix_gpu:
    Learning big matrices can be a hard task. Therefore running the code on CPU can be a slow process. This file runs the learning proccess on 
    GPU instead of CPU. To train the simulator run the following command:
    test = Test()
    test.run_tests()
    
**Running the Simulator:**
    You can find the model file after training the Simulator in the "Saved Models" folder inside of the "Results" folder.
    To run the simulation from the learnt model run the following code:
    test = Test()
    test.export_to_classifier(model_name) - where model name should be the name of the model as appears in the folder
    You can find the results under the "Outputs" folder that is inside of the "Results" folder.
    
**Using different structures for the Gan network:**
   In order to create a new model your need to create a new def in
   the class of GeneratorStructureFactory (e.g. structure_1 and create model and name for the structure.
   return the value in this new function as a GeneratorStructure which gets name and model in init
   Afterwards add "structure_list.append(self.yourList())" to the function of create_strucute_list