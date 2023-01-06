from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

       
      
# preOrder : first comes the root then its left node (or left tree) and then its right node (or tree)
def preOrder(root):
	# Your code goes here
    if root==None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
    
# postOrder : first comes the root's left node (or left tree) then its right node (or tree) and then the root itself
def postOrder(root):
	#Your code goes here
    if root==None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")
    
    
# InOrder : first comes the root's left node (or left tree) then the root itself and then its right node (or tree)   
def InOrder(root):
	#Your code goes here
    if root==None:
        return
    InOrder(root.left)
    print(root.data,end=" ")
    InOrder(root.right)
    
    
    

'''#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

# Main
root = takeInput()
preOrder(root)'''
