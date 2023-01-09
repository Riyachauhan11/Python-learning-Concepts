'''root is at depth 0 and the level right under root is at depth 1 so the depth increases 
the further we move down in the tree as per the level.'''

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

def PrintDepthK(root,k):
    if root==None:
        return
    if k==0:
        print(root.data)
        return 
    PrintDepthK(root.left,k-1)
    PrintDepthK(root.right,k-1)


def PrintDepthK2(root,k,d=0):
    if root==None:
        return
    if k==d:
        print(root.data)
        return 
    PrintDepthK2(root.left,k,d+1)
    PrintDepthK2(root.right,k,d+1)


root=treeInput()
PrintTreeDetailed(root)
PrintDepthK2(root,2)
