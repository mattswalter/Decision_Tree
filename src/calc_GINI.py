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
def calculate_GINI(data, column_names, target="Class"):
    """Calculate GINI for each attribute in the data and return the max"""

    GINI_SET = calculate_class_GINI(data[target])
    
    initialize = [None] * len(column_names)
    gini_dict = dict(zip(column_names, initialize))

    for key in column_names:  
          
        #Get locations where ....
        get_X1 = data[target].loc[data[key] == 1]
        get_X0 = data[target].loc[data[key] == 0]
    
        #Count the 1's and 0's based on indexes found
        X1 = get_X1.value_counts().to_dict()
        X0 = get_X0.value_counts().to_dict()
        
        if len(list(X1.keys())) <= 1 or len(list(X0.keys())) <= 1:
            if len(list(X1.keys())) < 1 and len(list(X0.keys())) < 1:
                gini_dict[key] = GINI_SET - 0
                
            else:
                if len(list(X1.keys())) > 1:
                    X = X1

                    P0 = X[1]
                    N0 = X[0]
                    
                    xt = P0+0+N0+0
                    
                    x1 = ((0+P0)/xt)*((P0/(P0+0))*(0/(P0+0)))
                    x0 = ((0+N0)/xt)*((N0/(N0+0))*(0/(N0+0)))

                    gini_dict[key] = GINI_SET - (x1+x0)
                    
                elif len(list(X0.keys())) > 1:
                    X = X0
                    
                    #Store the count of class 1's - Yes / 0's - No
                    P0 = X[1]
                    N0 = X[0]
                    
                    xt = P0+0+N0+0
                    
                    # x1 = (count x = 1 / total x count)(count: x = 1 and class = 0 / total x = 1 * count: x = 1 and class = 1 / total x = 0)
                    x1 = ((0+P0)/xt)*((P0/(P0+0))*(0/(P0+0)))
                    x0 = ((0+N0)/xt)*((N0/(N0+0))*(0/(N0+0)))

                    gini_dict[key] = GINI_SET - (x1+x0)
                    
                else:
                    
                    gini_dict[key] = GINI_SET - 0
                    
        else:
               #Store the count of class 1's - Yes /  0's - No
                P1 = X1[1]
                N1 = X1[0]

                #Store the count of class 1's - Yes /  0's - No
                P0 = X0[1]
                N0 = X0[0]
                
                xt = P0+P1+N0+N1
                
                # x1 = (count x = 1 / total x count)(count: x = 1 and class = 0 / total x = 1 * count: x = 1 and class = 1 / total x = 0)
                x1 = ((P1+P0)/xt)*((P0/(P0+P1))*(P1/(P0+P1)))
                x0 = ((N1+N0)/xt)*((N0/(N0+N1))*(N1/(N0+N1)))
                gini_dict[key] = GINI_SET - (x1+x0)

    parent_node_class_V = max(gini_dict, key=gini_dict.get)  # Just use 'min' instead of 'max' for minimum.
    #print("MAX Impurity: ", parent_node_class_V, vimp_dict[parent_node_class_V])       

    return parent_node_class_V


def calculate_class_GINI(class_data):
    """Calculate GINI of the CLASS data"""
    K = len(class_data)
    tmp = class_data.value_counts().to_dict()
    K0 = tmp[0]#K =0
    K1 = tmp[1]#K=1
    
    # Class Impurity = pt = k0/total * k1/total : class = 0 / total class * class = 1 / total class
    pt = (K0 / (K)) * (K1 / (K))
    return pt