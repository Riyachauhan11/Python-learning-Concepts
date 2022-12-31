'''Input Format:

The first line contains an integer 'q' which denotes 
the number of queries to be run against each operation on the queue. 
Then the test cases follow.

Every 'q' lines represent an operation that needs to be performed.

For the enqueue operation, the input line will contain two integers separated by a single space, 
representing the type of the operation in integer and the integer data being enqueued into the queue.

For the rest of the operations on the queue, the input line will contain only one integer value,
representing the query being performed on the queue.


Output Format:

For Query-1, you do not need to return anything.
For Query-2, prints the data being dequeued from the queue.
For Query-3, prints the data kept on the front of the queue.
For Query-4, prints the current size of the queue.
For Query-5, prints 'true' or 'false'(without quotes).

Output for every query will be printed in a separate line.'''







from sys import stdin


#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.__head=None
        self.__tail= None
        self.__count = 0

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self) :
        #Implement the getSize() function
        return self.__count


    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.getSize()==0


    def enqueue(self, data) :
        #Implement the enqueue(element) function
        new_node = Node(data)
        if self.__head is None:
            self.__head=new_node
        else:
            self.__tail.next=new_node
        self.__tail=new_node
        self.__count += 1


    def dequeue(self) :
        #Implement the dequeue() function
        if self.isEmpty():
            return -1
        else:
            element=self.__head.data
            self.__head=self.__head.next
            self.__count -= 1
            return element


    def front(self) :
        #Implement the front() function
        if self.isEmpty():
            return -1
        else:
            return self.__head.data




#main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2 :
        print(queue.dequeue())

    elif choice == 3 :
        print(queue.front())

    elif choice == 4 : 
        print(queue.getSize())

    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
