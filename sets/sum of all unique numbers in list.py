def sum_unique(l):
    s=set() #empty set
    for number in l:
        s.add(number)
    sum=0
    for i in s:
        sum+=i
    print(sum)

sum_unique([1,2,3,4,1,2,3,4,1,2,3,4])
