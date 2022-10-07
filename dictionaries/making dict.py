a={'the':3,'a':5,10000:'value','dict':{3:4},'li':[1.2,3]}
print(type(a))
print(len(a))

#making dictionaries
b=a.copy()
print(b)
c=dict([{'apples',3},{'pear',4},{'cherry',2}])
print(c)
d=dict.fromkeys(['a','b','c'],11)
print(d)
