str=input().split()
n,m=int(str[0]),int(str[1])
li=[[int(j) for j in input().split()] for i in range(n)]
print(li)
#for jagged list remove m and str from above and take n as int input

str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
li2=[[int(b[m*i+j]) for j in range(m)] for i in range(n)]
print(li2)
