a={1,2,3,4}
b={3,4,5,6}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b))

#update methods changes the set onto which they are being applied on
#update cant be used with union
a.intersection_update(b)
print(a)
a={1,2,3,4}
a.difference_update(b)
print(a)
a={1,2,3,4}
a.symmetric_difference_update(b)
print(a)

a={1,2,3,4}
b={3,4,5,6}
c={3,4}
d={88}
print(a.issubset(b))
print(c.issubset(a))
print(a.issuperset(c))
print(b.issuperset(c))
print(a.isdisjoint(d))