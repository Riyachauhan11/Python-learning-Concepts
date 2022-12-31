class Queue:

    def __init__(self):
        self.__data = []
        self.__front = 0
        self.__count = 0

    def enqueue(self, item):
        self.__data.append(item)
        self.__count += 1

    def dequeue(self):
        if self.isEmpty():
            print("Hey! queue is empty.")
            return
        element = self.__data[self.__front]
        self.__front = self.__front+1
        self.__count -= 1
        return element

    def first(self):
        if self.isEmpty():
            print("Hey! queue is empty.")
            return
        return self.__data[self.__front]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while (q.isEmpty() is False):
    print(q.first())
    q.dequeue()

q.dequeue()
