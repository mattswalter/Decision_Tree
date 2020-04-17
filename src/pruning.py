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
import copy
import random
from src.calculateAccuracy import calculateAccuracy
    
def post_pruning(validation_set_arg, Tree, K_arg, L_arg):
    """ PRUNE THE TREE GIVEN VALIDATION AND K & L Integer"""
    
    ppDTree = copy.deepcopy(Tree)
    ogTreeAccuracy = calculateAccuracy(validation_set_arg,ppDTree)
    
    #idx and jdx will never be used just an loop control
    for idx in range(1,L_arg): #1 to L
        CTree2 = copy.deepcopy(Tree)       
        for jdx in range(1,random.randint(1,K_arg)): # 1 to M
            nonLeafNodeList = CTree2.getNonLeafNodeList()
            N = len(nonLeafNodeList)
            
            if N <= 0:
                break
            
            P = random.randint(0, N-1)
            node_P = nonLeafNodeList[P]
            node_P.left = node_P.right = None
        
            if node_P.N > node_P.P:
                node_P.data = '0'
            else:
                node_P.data = '1'
            
        newTreeAccuracy = calculateAccuracy(validation_set_arg,CTree2)
        
        if newTreeAccuracy > ogTreeAccuracy:
            ppDTree = copy.deepcopy(CTree2)
            ogTreeAccuracy = newTreeAccuracy
        #ELSE USE ORIGINAL
        
    return ppDTree