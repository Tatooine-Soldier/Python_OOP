class Node:                                       #Node builder
    def __init__(self, element):
        self._element = element
        self._rchild = None
        self._lchild = None
        
class BST:
    def __init__(self):
        self._root = None
        
    def addRoot(self, root):                                    #build the bst, so add a root first
        self._root = root
        
        
    def addToTree(self, node):
        if self._root._element < node._element:                 #if root node value is less than node you adding 
            if self._root._rchild is None:                      #add as right child if None
                self._root._rchild = node._element
            else:
                self._root._rchild.add(node)                    #else keep searching right for a None space
                self._root = self._root._rchild                 #root child 'becomes' root, i.e. working down the tree 
        else:
            if self._root._lchild is None:
                self._root._lchild = node._element
            else:
                self._.root._lchild.add(node)
                self._root = self._root._lchild                 #root child 'becomes' root, i.e. working down the tree 
                
    def printRoot(self):
        print(self._root)                                       #print the root
                
    def printNode(self, node):                                  #print the selected node and its children
        print(node._element)
        print(node._rchild)
        print(node._lchild)
        
        
        
myBst = BST()  
two = Node(2)
myBst.addRoot(two)

one = Node(1)     

three = Node(3)
myBst.addToTree(three)
myBst.addToTree(one)
myBst.printNode(two)
