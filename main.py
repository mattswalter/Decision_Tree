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
# #  Command Line Execution:
# #      python main.py 7 7 training_set.csv validation_set.csv test_set.csv yes
# =============================================================================

from __future__ import print_function
import os, sys           
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.execute import execute

def main():
    if len(sys.argv) < 7:
        print("INVALID INPUT")
        print("python main.py <L> <K> <training_set> <validation_set> <test_set> <to-print>")
        sys.exit(0)
    else:
        yes_no = False
        if str((sys.argv[6])).upper() == "YES":
            yes_no = True
    
    execute(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5],yes_no )

if __name__ == "__main__":  
    main()