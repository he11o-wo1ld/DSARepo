# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
		return getLeftMostChild(node.right)
	return getRightMostChild(node)
 
def getLeftMostChild(node):
	currentNode = node
	while currentNode.left is not None:
		currentNode = currentNode.left
	return currentNode

def getRightMostChild(node):
	currentNode = node
	while currentNode.parent is not None and currentNode.parent.right == currentNode:
		currentNode = currentNode.parent
	return currentNode.parent