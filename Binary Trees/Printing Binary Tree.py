class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def PrintTree(root):
    if root==None:
        return
    print(root.data)
    PrintTree(root.left)
    PrintTree(root.right)


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


btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)
btn4 = BinaryTreeNode(4)
btn5 = BinaryTreeNode(5)

btn1.left = btn2
btn1.right = btn3
btn2.left=btn4
btn2.right=btn5

PrintTreeDetailed(btn1)
