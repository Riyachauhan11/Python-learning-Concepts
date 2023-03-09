import heapq

#creates heap
li=[1,5,4,8,7,9,11]
heapq.heapify(li)
print(li)

#inserts element of your choice into heap
heapq.heappush(li,2)
print(li)

#removes min priority element from heap
print(heapq.heappop(li))
print(li)

#replaces the min priority element with the given element and heapify the heap
heapq.heapreplace(li,6)
print(li)
heapq.heapreplace(li,10)
print(li)