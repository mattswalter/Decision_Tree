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
import math

def calculate_entropy(data, column_names, target="Class"):
    """
    Calculate Entropy/Gain for each attribute in the data and return the max GAIN
    
    Use the class data to calculate the entropy of the set
    
    Then use the attribute and class columns, calculate the Positives and Negatives
    
    Calculate Entropy
    
    Calculate Average Info
    
    Use average info and Entropy of the set to return Gain

    P1 = Positive Class Value, Attribute with a 1
    P0 = Positive Class Value, Attribute with a 0

    N1 = Negative Class Value, Attribute with a 1
    N0 = Negative Class Value, Attribute with a 0

    Ps = Of the class values, count of positive (1) values
    Ns = Of the class values, count of negative (0) values
    """

    EntropyS, Ps, Ns = calculate_class_entropy(data[target])
    #print("Class Entropy: ", EntropyS)

    initialize = [None] * len(column_names)
    gain_dict = dict(zip(column_names, initialize))

    for key in column_names:         
        #In the Class data column ... Where attribute data is 0
        get_X1 = data[target].loc[data[key] == 1]
        get_X0 = data[target].loc[data[key] == 0]
    
        #Count the 1's and 0's
        X1 = get_X1.value_counts().to_dict()
        X0 = get_X0.value_counts().to_dict()
        
        if len(list(X1.keys())) <= 1 or len(list(X0.keys())) <= 1:
            if len(list(X1.keys())) < 1 and len(list(X0.keys())) < 1:
                Average_Info = 0
            else:
                if len(list(X1.keys())) > 1:
                    X = X1
                    N0 = X[0]
                    P0 = X[1]
                    Entropy0 = (-P0/(P0+N0))*math.log2(P0/(P0+N0)) - (N0/(P0+N0))*math.log2(N0/(P0+N0))
                    Average_Info = 0 + (P0+N0)/(Ps + Ns) * Entropy0
                    
                elif len(list(X0.keys())) > 1:
                    X = X0
                    N0 = X[0]
                    P0 = X[1]
                    Entropy0 = (-P0/(P0+N0))*math.log2(P0/(P0+N0)) - (N0/(P0+N0))*math.log2(N0/(P0+N0))
                    Average_Info = 0 + (P0+N0)/(Ps + Ns) * Entropy0
                else:
                    Average_Info = 0
        else:
            #Store the count of class 1's - Yes
            P1 = X1[1]
            #Store the count of class 0's - No
            N1 = X1[0]

            #Store the count of class 1's - Yes
            P0 = X0[1]
            #Store the count of class 0's - No
            N0 = X0[0]
            
            #Calculate Entropy for the 1's
            Entropy1 = (-P1/(P1+N1))*math.log2(P1/(P1+N1)) - (N1/(P1+N1))*math.log2(N1/(P1+N1))
            
            #Calculate Entropy for the 0's
            Entropy0 = (-P0/(P0+N0))*math.log2(P0/(P0+N0)) - (N0/(P0+N0))*math.log2(N0/(P0+N0))
        
            #Calculate the Average Information
            Average_Info = (P1+N1)/(Ps + Ns) * Entropy1 + (P0+N0)/(Ps + Ns) * Entropy0

        gain_dict[key] = calculate_gain(EntropyS, Average_Info)        
        
    parent_node_class_G = max(gain_dict, key=gain_dict.get)  # Just use 'min' instead of 'max' for minimum.

    #print("MAX Gain: ", parent_node_class_G, gain_dict[parent_node_class_G])    
    
    return parent_node_class_G  


    
def calculate_class_entropy(column):
    """Calculate Entropy for the entire class variable"""
    counts = column.value_counts().to_dict()
    Ps = counts[1] # 1 values
    Ns = counts[0] # 0 values
    
    #Entropy Function
    EntropyS = (-Ps/(Ps+Ns))*math.log2(Ps/(Ps+Ns)) - (Ns/(Ps+Ns))*math.log2(Ns/(Ps+Ns))
    
    return EntropyS, Ps, Ns


def calculate_gain(EntropyS, Average_Info):
    """Calculate Gain"""
    return EntropyS - Average_Info   