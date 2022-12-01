#   Time complexity - O(n)

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    while head is not None:
        print(str(head.data)+"->", end="")
        head = head.next
    print("None")
    return


def takeInput():

    head = None
    tail = None
    input_list = [int(ele) for ele in input().split()]
    for currdata in input_list:

        if currdata == -1:
            break

        newNode = Node(currdata)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


head = takeInput()
printLL(head)
