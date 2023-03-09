import heapq

#creates heap
li=[1,5,4,7,8,9,2,3]
heapq._heapify_max(li)
print(li)

#removes max priority element from heap
print(heapq._heappop_max(li))
print(li)

#replaces the max priority element with the given element and heapify the heap
heapq._heapreplace_max(li,0)
print(li)

#inserts element of your choice into heap
li.append(6)
heapq._siftdown_max(li,0,len(li)-1)
print(li)

