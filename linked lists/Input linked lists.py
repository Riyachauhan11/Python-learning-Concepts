class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():

    input_list = [int(ele) for ele in input().split()]
    head = None
    for currdata in input_list:

        if currdata == -1:
            break

        newNode = Node(currdata)
        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode

    return head


head = takeInput()
print(head)
