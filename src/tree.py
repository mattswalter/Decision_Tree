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

class Node:
    """NODE CLASS"""
    def __init__(self, value, node, N, P):
        self.left = None
        self.right = None
        self.data = value #Attribute Name
        self.N = N
        self.P = P
        self.node = node

class Tree:
    """TREE CLASS - TREE FULL OF NODES"""
    def __init__(self):
        self.root = None
        self._branch = None
        self.counter = 0
        self.nonLeafList =list()
    
    def getRoot(self):
        return self.root


    def getRight(self,node):
        if(node!=None):
            return node.right

            
    def setRight(self, node, value, N, P):
        self.counter+=1
        if(self.root == None):
            self.root = Node(value,self.counter,N,P)
        else:
            self._find(node, self.root)
            self._branch.right = Node(value,self.counter,N,P)
        return self.counter
    
    
    def getLeft(self,node):
        if(node!=None):
            return node.left
            
        
    def setLeft(self, node, value, N, P):
        self.counter+=1
        if(self.root == None):
            self.root = Node(value,self.counter,N, P)
        else:           
            self._find(node, self.root)
            self._branch.left = Node(value,self.counter,N,P)
        return self.counter
        
        
    def setValue(self,ID,value):
        self._find(ID, self.root)
        self._branch.data = value
        
        
    def _find(self, count, root):       
        if(root.node == count): 
            self._branch = root
        else:
            if(root.left !=None):
                self._find(count,root.left)
            if(root.right != None):
                self._find(count,root.right)
        return


    def _printTree(self, root):
        if(root.left!=None): 
            tmpStr = ""
            # FOR EACH BRANCH ADD A LINE
            for i in range(0,self._branch):
                # Add a line.....
                tmpStr= tmpStr+"| "
            #check if left child is a leaf
            if(root.left != None and root.left.left==None and root.left.right==None):
                write_out = tmpStr+str(root.data)+" = 0 : "+str(root.left.data)
                print(write_out)               
            else:
                write_out = tmpStr+str(root.data)+" = 0 : "
                print(write_out)
                
                self._branch+=1
                self._printTree(root.left)
                self._branch-=1
                
        if(root.right!=None): 
            tmpStr = ""
            # FOR EACH BRANCH ADD A LINE
            for i in range(0,self._branch):
                tmpStr= tmpStr+"| "
            #check if right child is a leaf
            if(root.right != None and root.right.left == None and root.right.right==None):
                write_out = tmpStr+str(root.data) + " = 1 : " + str(root.right.data)
                print(write_out)              
            else:
                write_out = tmpStr+str(root.data)+" = 1 : "
                print(write_out)
                
                self._branch+=1
                self._printTree(root.right)
                self._branch-=1
        
            
    def printTree(self):
        self._branch = 0
        if(self.root != None):
            if(self.root.left == None and self.root.right == None):
                print(self.root.data)
            else:
               self._printTree(self.root) 


    def traversal(self,root,node):
        if(self.getLeft(root)==None and self.getRight(root)==None):
            return int(root.data)
        elif(node[root.data]==0):            
            return int(self.traversal(self.getLeft(root),node))       
        else:
            return int(self.traversal(self.getRight(root),node))
        
            
    ### ADD FOR PRUNING
    def getNonLeafNodeList(self):
        self.nonLeafList = list()
        self._getNonLeafList(self.root)
        return self.nonLeafList
    
    def _getNonLeafList(self,root):
        if(root.right!=None or root.left!=None):
            self.nonLeafList.append(root)
        if(root.right!=None):
            self._getNonLeafList(root.right) #RECURSION
        if(root.left!=None):
            self._getNonLeafList(root.left) #RECURSION
        return
    
    #NEED THIS TO CREATE THE IMPURITY TREE. REMOVE ENTROPY. THEN MAKE A NEW ONE
    def deleteTree(self):
        self.root = None