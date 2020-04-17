# =============================================================================
# #
# #  Created on Thu Sep 19 18:00:56 2019
# #
# #  CISC684: Group 2
# #
# #  @author: Eric Allen <allenea@udel.edu>
# #           Matthew Walter <mswalter@udel.edu>
# #           Murugesan Somasundaram <smuruges@udel.edu>
# #           
# =============================================================================
#IMPORTS
import sys
import src.tree as T
import pandas as pd
from src.ID3 import ID3
from src.pruning import post_pruning
from src.calculateAccuracy import calculateAccuracy

def execute(L, K, training_set_arg, validation_set_arg, test_set_arg, to_print_arg):
    """ Create the Entropy Binary Tree, Print, Prune, Print, Stats, Delete, Create 
    Variance Impurity Binary Tree, Print, Prune, Print, Stats
    
    for a given training, validation and testing dataset
    
    L and K are used for printing
    
    Print?
    """
    
    #Make Tree Object
    BinaryTree = T.Tree()
    
    training = pd.read_csv(training_set_arg,low_memory=True)
    validation = pd.read_csv(validation_set_arg,low_memory=True)
    testing = pd.read_csv(test_set_arg,low_memory=True)
    
    column_names = training.columns
    
    #Make sure they are integers
    if K.isdigit() and L.isdigit():
        K_arg = int(K)
        L_arg = int(L)
    else:
        print("L or K integer is not a numerical value....Exiting....")
        sys.exit(0)
    
    if len(training) == 0:
        print("Empty Dataset!....Exiting....")
        sys.exit(0)    
            
    ID3(BinaryTree, training, column_names, None, "entropy",target="Class")
    
    if to_print_arg == True:
        print("Printing Entropy Tree")
        print(BinaryTree.printTree())
    
    pruned_tree = post_pruning(validation, BinaryTree, K_arg, L_arg)
    
    if to_print_arg == True:
        print("Printing Prunned Entropy Tree")
        print(pruned_tree.printTree())
        
        
    print("Accuracy before pruning - Entropy:  ",calculateAccuracy(testing,BinaryTree))
    print("Accuracy after pruning - Entropy:   ", calculateAccuracy(testing,pruned_tree)) 
        
    #Delete tree and start again for Variance Impurity
    BinaryTree.deleteTree()  
    
    #Make tree for Variance Impurity
    BinaryTree = T.Tree()
    ID3(BinaryTree, training, column_names, None, "GINI",  target="Class")
    
    if to_print_arg == True:
        print("Printing Variance Impurity Tree")
        print(BinaryTree.printTree())
    
    pruned_tree2 = post_pruning(validation, BinaryTree, K_arg, L_arg)
    
    if to_print_arg == True:
        print("Printing Variance Impurity Tree")
        print(pruned_tree2.printTree())
    
    print("Accuracy before pruning - Variance Impurity:  ",calculateAccuracy(testing,BinaryTree))
    print("Accuracy after pruning - Variance Impurity:   ", calculateAccuracy(testing,pruned_tree2))