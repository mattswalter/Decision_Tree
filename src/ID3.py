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
from src.calc_Entropy import calculate_entropy
from src.calc_GINI import calculate_GINI

def ID3(BinaryTree, data, columns,parent_node_class, calculate, target="Class"):
    """ ID3 Algorithm for either Entropy or GINI"""
    if parent_node_class == None:
        column_names = list(columns)
        column_names.remove("Class")
    else:
        column_names = list(columns)    
    
    P = len(data.loc[data['Class'] == 1])
    N = len(data.loc[data['Class'] == 0])
    
    #If All Negative
    if P == 0:
        return '0'
    
    #If All Positive
    elif N == 0:
        return '1'
    
    #If length Feature Atrtribute is Empty
    elif len(data) == 0 or len(column_names) == 0:
        return data["Class"].unique()
        
    #Grow the tree
    else:        
        #for key in column_names:
        if calculate == "entropy":
            new_node = calculate_entropy(data, column_names)
            
        elif calculate == "GINI":
            new_node = calculate_GINI(data, column_names)

        if  parent_node_class == None:
            parent_node_class = BinaryTree.setLeft(None,new_node, N, P)

        for each in [0,1]:
            if new_node == 0 or new_node == 1:
                new_node = str(new_node)
                if P < N:
                    if each == 1:
                        BinaryTree.setRight(parent_node_class,new_node,N,P)
                    else:
                        BinaryTree.setLeft(parent_node_class,new_node,N,P)
                else:
                    if each == 1:
                        BinaryTree.setRight(parent_node_class,new_node,N,P)
                    else:
                        BinaryTree.setLeft(parent_node_class,new_node,N,P)
            else:
                rows = data.loc[data[new_node] == each]
                
                if new_node in column_names:
                    column_names.remove(new_node)
                if each == 1:                     
                    node = BinaryTree.setRight(parent_node_class,new_node,N,P)
                    rightNode = ID3(BinaryTree, rows,list(column_names), node, calculate)
                    BinaryTree.setValue(node,rightNode)
                else:                        
                    node = BinaryTree.setLeft(parent_node_class,new_node,N,P)
                    leftNode = ID3(BinaryTree, rows,list(column_names), node, calculate)
                    BinaryTree.setValue(node,leftNode)
                    
        return new_node