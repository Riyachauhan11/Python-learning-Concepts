class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PrintTreeDetailed(root):
    if root==None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L", root.left.data, end=",")
    if root.right != None:
        print("R", root.right.data,end=" ")
    print()
    PrintTreeDetailed(root.left)
    PrintTreeDetailed(root.right)


def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None

    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root


def takeLevelWiseTreeInput():
    q=queue.Queue()
    print("enter root: ")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while not (q.empty()):
        current_node=q.get()
        print("enter left child of ",current_node.data)
        leftChildData=int(input())
        if leftChildData != -1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)

        print("enter right child of ",current_node.data)
        rightChildData=int(input())
        if rightChildData != -1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)

    return root
    


root=treeInput()
PrintTreeDetailed(root)
