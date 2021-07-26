class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def findSecondMaxinBST(headNode):
    curNode = headNode
    secondMaxNode = None
    while curNode.right:
        secondMaxNode = curNode
        curNode = curNode.right
    
    if curNode.left:
        curNode = curNode.left
        while curNode.right:
            curNode = curNode.right
        secondMaxNode = curNode
    
    return secondMaxNode



treeNode = Node(5)
treeNode.left = Node(2)
treeNode.right = Node(7)
treeNode.right.left = Node(6)
secondMax = findSecondMaxinBST(treeNode)
if secondMax:
    print(secondMax.data)
else:
    print("only one element bst")