class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()


def takeTreeInput():
    print("enter root data")
    rootdata=int(input())
    if rootdata==-1:
        return None
    
    root=TreeNode(rootdata)

    print("enter number of children for ",rootdata)
    childrenCount=int(input())
    for i in range(childrenCount):
        child=takeTreeInput()
        root.children.append(child)

    return root


def takeTreeInputLevelWise():
    q=queue.Queue()
    print("enter root")
    rootData=int(input())
    if rootData==-1:
        return None
    
    root=TreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node=q.get()
        print("Enter num of children for ",current_node.data)
        numChildren=int(input())
        for i in range(numChildren):
            print("Enter next child for ",current_node.data)
            childData=int(input())
            child=TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    return root


'''printing data in preorder'''
def printTree(root):

    #not a base case but an edge case
    if root==None:
        return 
    
    print(root.data)
    #for loop takes care of leaf nodes (hence why we dont need a base case)
    for child in root.children:
        printTree(child)


'''printing data in detail'''
def printTreeDetailed(root):
    if root==None:
        return
    
    print(root.data,end=':')
    
    for child in root.children:
        print(child.data,end=',')
    print()

    for child in root.children:
        printTreeDetailed(child)
        
root=takeTreeInput()
printTreeDetailed(root)

