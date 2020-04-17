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
def calculateAccuracy(validation_set_arg,Tree):
    """Calculate accuracy statistic"""
    root = Tree.getRoot()
    
    X = validation_set_arg.iloc[:,:-1]
    treeRes = []
    count = 0
    
    for index, row in X.iterrows():
        posit = Tree.traversal(root,row)
        treeRes.append(posit)
        if posit == validation_set_arg['Class'][index]:
            count+=1
    
    return (count/len(validation_set_arg))*100