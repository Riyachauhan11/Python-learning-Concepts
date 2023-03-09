from sys import stdin


class QueueUsingTwoStacks:

    # Define data members and __init__()
    def __init__(self):
        self.__stk1 = []
        self.__stk2 = []

    '''----------------- Public Functions of Queue -----------------'''

    def getSize(self):
        return len(self.__stk1)

    def isEmpty(self):
        return len(self.__stk1) == 0

    def enqueue(self, data):
        self.__stk1.append(data)

    def dequeue(self):
        if self.isEmpty():
            return -1
        while len(self.__stk1) != 1:
            last_ele = self.__stk1.pop()
            self.__stk2.append(last_ele)
        deleted_ele = self.__stk1.pop()
        while len(self.__stk2) != 0:
            last_ele = self.__stk2.pop()
            self.__stk1.append(last_ele)
        return deleted_ele

    def front(self):
        if self.isEmpty():
            return -1
        return self.__stk1[0]


# main
q = int(stdin.readline().strip())

queue = QueueUsingTwoStacks()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2:
        print(queue.dequeue())

    elif choice == 3:
        print(queue.front())

    elif choice == 4:
        print(queue.getSize())

    else:
        if queue.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
