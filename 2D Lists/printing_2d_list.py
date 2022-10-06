string=input().split()
n,m=int(string[0]),int(string[1])
b=input().split()
li=[[int(b[m*i+j]) for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(li[i][j],end=' ')
    print()
#wont work on jagged lists

for row in li:
    for ele in row:
        print(ele,end=' ')
    print()


for row in li:
    output=' '.join([str(ele) for ele in row])
    print(output)