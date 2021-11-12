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
            return inorderList
        
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
            return preorderList
    
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
            return postorderList
    
    def printPostorderList(self, node, list):
        if node is not None:
            self.printPostorderList(node.left, list)
            self.printPostorderList(node.right, list)
            list.append(node.data)

    def countLeaves(self):
        leafList = []
        if self.root is not None:
            self.countLeavesList(self.root, leafList)
            return len(leafList)
        else:
            return 0
   
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
    try:

        tree = Tree()
    # for value in [5, 3, 4, 9, 1, 6]:
        #    tree.add(value)
        # [1,2,3,4,5,6,7,8]
        # [7,2,11,5,10,3,6,9,1,8]
        #["1","P","","50","200","40", "A", "#", "!", " ",""]
        #7,2,11,5,10,3,6,9,1,8
        #10,9,8,7,6,5,4,3,2,1
        for value in [5, 3, 4, 9, 1, 6]:
            tree.add(value)

        print("Original")
        tree.printTree()
        print("Inorder")
        print(tree.printInorderTree())
        print("Preorder")
        print(tree.printPreorderTree())
        print("Postorder")
        print(tree.printPostorderTree())
        print("count leaves")
        print(tree.countLeaves())
    except TypeError:
        print("Type str and int can't be mixed.")
    except:
        print("Something went wrong, please check the input.")


### ---------------------------- ### 
###             TESTS            ###
### ---------------------------- ### 

def testCase(testNumber, list, expectedResultPreorder, expectedResultInorder, expectedResultPostorder, expectedLeafCount):
    try:

        tree = Tree()
        for value in list:
            tree.add(value)

        actualResultPreorder = tree.printPreorderTree()
        actualResultInorder = tree.printInorderTree()
        actualResultPostorder = tree.printPostorderTree()
        actualLeafCount = tree.countLeaves()
        
        if actualResultPreorder == expectedResultPreorder:
            print("Test", testNumber, "passed for pre-order.")
        else:
            print("Test", testNumber, "failed for pre-order.")

        if actualResultInorder == expectedResultInorder:
            print("Test", testNumber, "passed for in-order.")
        else:
            print("Test", testNumber, "failed for in-order.")

        if actualResultPostorder == expectedResultPostorder:
            print("Test", testNumber, "passed for post-order.")
        else:
            print("Test", testNumber, "failed for post-order.")
        
        if actualLeafCount == expectedLeafCount:
            print("Test", testNumber, "passed the leaf count.")
        else:
            print("Test", testNumber, "failed the leaf count.")

    except TypeError:
        print("Test", testNumber,"could not be performed because type str and int can't be mixed.")
    except:
        print("Something went wrong, please check the input.")    


def test():
    testCase(1, [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [8,7,6,5,4,3,2,1], 1)
    print()
    testCase(2, [7,2,11,5,10,3,6,9,1,8], [7, 2, 1, 5, 3, 6, 11, 10, 9, 8], [1, 2, 3, 5, 6, 7, 8, 9, 10, 11], [1, 3, 6, 5, 2, 8, 9, 10, 11, 7],4)
    print()
    testCase(3, [], None, None, None, 0)
    print()


def myTests():
    print("Additional Tests.")
    testCase(4, [3], [3], [3], [3],1)
    print()
    testCase(5, ["D","B","C","F","A","E","G"], ["D","B","A","C","F","E","G"], ["A","B","C","D","E","F","G"], ["A","C","B","E","G","F","D"],4)
    print()
    testCase(6, [10,9,8,7,6,5,4,3,2,1], [10,9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10], 1)
#main()
test()
myTests()