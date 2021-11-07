### File: TreeTraversal.py
### Author: Samuel Rudqvist
### CSCI 0262 Algorithms
### 
###
### 
### Modification Log:
### 
###

### ---------------------------- ### 
###        The Node Class        ###
### ---------------------------- ### 
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


### ---------------------------- ### 
###        The Tree Class        ###
### ---------------------------- ###
class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.addNode(value, self.root)
    
    def addNode(self, value, node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self.addNode(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.addNode(value, node.right)

    def find(self, value):
        if self.root is None:
            return None
        else:
            self.findNode(value, self.root)

    def findNode(self, value, node):
        if node is None:
            return None
        if value == node.data:
            return node
        elif value < node.data:
            self.findNode(value, node.left)
        elif value > node.data:
            self.findNode(value, node.right)

    def printTree(self):
        if self.root is not None:
            self.printTreeFromNode(self.root)

    def printTreeFromNode(self, node):
        if node is not None:
            self.printTreeFromNode(node.left)
            print(str(node.data))
            self.printTreeFromNode(node.right)

    # Add all nodes inorder to a list and then print the list
    def printInorderTree(self):
        if self.root is not None:
            inorderList = []
            self.printInorderList(self.root, inorderList)
            print(inorderList)
        
    def printInorderList(self, node, list):
        if node is not None:
            self.printInorderList(node.left, list)
            list.append(node.data)
            self.printInorderList(node.right, list)
            
    # Preorder
    def printPreorderTree(self):
        if self.root is not None:
            preorderList = []
            self.printPreorderList(self.root, preorderList)
            print(preorderList)
    
    def printPreorderList(self, node, list):
        if node is not None:
            list.append(node.data)
            self.printPreorderList(node.left, list)
            self.printPreorderList(node.right, list)
    
    # Postorder
    def printPostorderTree(self):
        if self.root is not None:
            postorderList = []
            self.printPostorderList(self.root, postorderList)
            print(postorderList)
    
    def printPostorderList(self, node, list):
        if node is not None:
            self.printPostorderList(node.left, list)
            self.printPostorderList(node.right, list)
            list.append(node.data)

    def countLeaves(self):
        leafList = []
        if self.root is not None:
            self.countLeavesList(self.root, leafList)
            print(len(leafList))
   
    def countLeavesList(self, node, leafList):
        if node is not None:
            
            if node.left is None and node.right is None:
                leafList.append(node.data)
            else:
                self.countLeavesList(node.left, leafList)
                self.countLeavesList(node.right, leafList)

                


   # def countNodes(node):
    #    print("here")
     #   if node is None:
      #      return 0
       # else:
        #    return countNodes(node.left) + countNodes(node.right) + 1

    #def findMin(node):
     #   node = Tree.getRoot(self)
      #  if node is not None:
       #     while node.left is not None:
        #        node = node.left
         #   print("Smallest value is:", node.data)



### ---------------------------- ### 
###       The Main Function      ###
### ---------------------------- ### 
def main():
    tree = Tree()
    for value in [5, 3, 4, 9, 1, 6]:
        tree.add(value)
    print("Original")
    tree.printTree()
    print("Inorder")
    tree.printInorderTree()
    print("Preorder")
    tree.printPreorderTree()
    print("Postorder")
    tree.printPostorderTree()
    print("count leaves")
    tree.countLeaves()
    
    # Find the smallest value in the tree
   # node = tree.getRoot()
    #if node is not None:
     #   while node.left is not None:
      #      node = node.left
       # print("Smallest value is:", node.data)

def test():
    pass

main()