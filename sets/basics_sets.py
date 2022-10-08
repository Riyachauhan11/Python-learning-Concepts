a={'apple','abc',123}
print(type(a))
print(len(a))

'''a[0] will throw an error since sets are not ordered and 
so would a[ele of set]'''
#print(a[0])
#print(a[123])

#in operator
print('apple' in a)
print('u' in a)

#for loops
for i in a:
    print(i) #might not display in the order of elements in set

#adding data to sets
a.add('riya')
print(a)
b={'ty','riya','oooo'}
a.update(b)
print(a)

#deleting data from sets
a.remove(123)
print(a)
'''if we put a value in sets that doesnt exist in it and 
use the remove method, it will throw an error.However doing the same
but with discard method will not throw an error and simply nothing
would be updated in the set. '''
#a.remove('rrr')
a.discard('rrr')
a.discard('abc')
print(a)
a.pop() #deletes any random ele
print(a)

#clearing whole set
a.clear()
print(a)

#deleting whole set
del a
#print(a)
