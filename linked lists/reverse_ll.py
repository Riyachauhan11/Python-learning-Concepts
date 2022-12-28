from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

# Following is the Node class already written for the Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# big time complexity
def reverse1(head):
    # Your code goes here
    if head is None or head.next is None:
        return head
    smallhead = reverseLinkedListRec(head.next)
    curr = smallhead
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return smallhead

  
#better time complexity  
def reverse1(head):
  if head is None or head.next is None:
      return head,head
  sh,st=reverse1(head.next)
  st.next=head
  head.next=None
  return sh,head

 
#further better (easier code)
def reverse3(head):
    if head is None or head.next is None:
        return head
    smallhead = reverse3(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return [smallhead, tail]

  
#iterative solution
def reverse4(head):
    # Write your code here
    curr=head
    prev=None
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head
  
  
  
# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()

    new_head, tail = reverse3(head)
    printLinkedList(reverse3(head)[0])

    t -= 1
