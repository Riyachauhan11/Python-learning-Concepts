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


def lengthLL(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count


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
printLL(head)
print(lengthLL(head))
