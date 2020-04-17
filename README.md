# CISC684_Decision_Tree
## BY: Eric Allen, Matthew Walter, Murugesan Somasundaram

Requires: Python3.6

Libraries: Pandas, os, sys, copy, math, random

Requires 7 arguments and training, validation, and test dataset csv files should be provided in the directory with main.py


#### L: integer (used in the post-pruning algorithm)
#### K: integer (used in the post-pruning algorithm)
#### training_set: valid file (.csv)
#### validation_set: valid file (.csv)
#### test_set: valid file (.csv)
#### to_print:{yes,no}


## To Run
 > python main.py <L> <K> <training_set> <validation_set> <test_set> <to_print> 
 
## Example Run
 > python main.py 7 7 training_set.csv validation_set.csv test_set.csv yes
