a=(1,2)
print(type(a))

#storing multiple values in a var returns a tuple in that variable
e=5,6
print(e)
print(type(e))

#works similar to a list
print(e[1])
f=(1,2,3,4,5,6)
print(f[3:])

#del f[4] or f[4]=8 results in an error since tuple is immutable
del f 
'''completely deleting a tuple is possible.'''
