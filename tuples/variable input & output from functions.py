def sum(a,b,c=0,d=0,e=0):
    return a+b+c+d+e

sum(1,2,3,4,5)

#using a *var as an input in function lets us input as many values as we want. 
#its of tuple type and is more convinient than the function above
def sum2(a,b,*more):
    print(a)
    print(b)
    print(type(more)) #tuple
    ans=a+b
    for i in more:
        ans=ans+i
    return ans

print(sum2(2,3,4,5))

def sum_diff(a,b):
    return a+b,a-b,a*b

#c is a tuple as its a single var storing multiple values
c=sum_diff(4,1)
print(c)

#need to be careful while writing multiple var for a function because if the count of var 
#doesnt match the number of values being returned from function an error will be thrown
d,e,f=sum_diff(4,1)
print(d)
