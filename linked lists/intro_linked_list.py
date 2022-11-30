class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(13)
b = Node(15)
a.next = b

print(a.data)
print(b.data)
print(a.next.data)

print(a)  # reference of a
print(b)  # reference of b
print(a.next)  # reference of b so both values r same

# print(b.next.data)
'''throws error as b.next points to None which has no data'''
