'''Implement a Stack Data Structure specifically to store integer data using a Singly Linked List.
(using linked lists)
The data members should be private.'''

'''Input Format:
The first line contains an integer 'q' which denotes the number of queries to be run against each operation in the stack. 
Then the test cases follow.

Every 'q' lines represent an operation that needs to be performed.

For the push operation, the input line will contain two integers separated by a single space, 
representing the type of the operation in integer and the integer data being pushed into the stack.

For the rest of the operations on the stack, the input line will 
contain only one integer value, representing the query being performed on the stack.


Output Format:
For Query-1, you do not need to return anything.
For Query-2, prints the data being popped from the stack.
For Query-3, prints the data kept on the top of the stack.
For Query-4, prints the current size of the stack.
For Query-5, prints 'true' or 'false'(without quotes).

Output for every query will be printed in a separate line.'''



from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :

    #Define data members and __init__()
    def __init__(self):
        self.__head=None
        self.__count=0


    '''----------------- Public Functions of Stack -----------------'''


    def getSize(self) :
        #Implement the getSize() function
        return self.__count


    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.getSize()==0



    def push(self, data) :
        #Implement the push(element) function
        newNode=Node(data)
        newNode.next=self.__head
        self.__head=newNode
        self.__count = self.__count +1



    def pop(self) :
        #Implement the pop() function
        if self.isEmpty():
            return -1
        data=self.__head.data
        self.__head = self.__head.next
        self.__count -=1
        return data


    def top(self) :
        #Implement the top() function
        if self.isEmpty():
            return -1
        return self.__head.data
        

#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
