#adding data to dict
a={'the':3,'a':5,10000:'value','dict':{3:4},'li':[1.2,3]}
a['tup']=(1,2,3) 
'''adds a new key value pair at end of dict a'''
print(a)

#updating data of dict
a['a']=4
print(a)
b={'the':4,'yes':7,'li':[1,2,3],'no':11}
(a.update(b))
print(a)

#deleting data from dict
a.pop(10000) 
'''dict.pop(correct key existing)
a.pop(0) will throw an error'''
print(a)
del a['the']
print(a)

#deleting all key value pairs from dict
a.clear()
print(a)

#deleting whole dict
del b
'''print(b) - will say b not defined since its been deleted'''
