a=(1,2,3)
b=4,5

# for loops
for i in a:
    print(i)

#in and len operators
print(1 in a)
print(1 in b)
print(len(a))

#Concatenations
c=a+b 
print(c)
#doesnt concatenate
d=(a,b)
print(d)

#repetition
e=a*4
print(e)

print(max(a))

a2=(1,2,(1,2))
a3=(1,2.2)

print(min(a3))

#list to tuple
l=[1,2,3,4]
tuple(l)
