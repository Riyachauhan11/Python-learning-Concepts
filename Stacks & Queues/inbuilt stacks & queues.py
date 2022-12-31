import queue

# inbuilt stack as list
s = [1, 2, 3]
s.append(4)
s.append(5)

print(s.pop())
print(s.pop())


# inbuilt queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

while not q.empty():
    print(q.get())


# using queue class to implement stack
stk = queue.LifoQueue()
stk.put(1)
stk.put(2)
stk.put(3)
stk.put(4)

while not stk.empty():
    print(stk.get())
