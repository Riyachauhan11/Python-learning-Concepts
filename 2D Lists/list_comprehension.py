li1=[1,2,3,4,5,6,7,8,9]
li_2=[ele for ele in li1 if ele%2==0 if ele%3==0]
li2=[1,2,3,4,5]
li_3=[ele**2 for ele in li2 if ele%2==0]
print(li_3)
li4=[1,2,3,4]
li5=[2,3,6,7,8]
li_4=[ele for ele in li4 for ele2 in li5 if ele==ele2]
print(li_4)
li_5=[ele for ele in li4 if ele in li5 and ele in li2]
print(li_5)
li_6=[ele**2 if ele%2==0 else ele for ele in li1]
print(li_6)
a='riya'
li_7=[let for let in a]
print(li_7)
li6=['riya','rohan','rohit']
li_8=[[s for s in ele] for ele in li6]
print(li_8)
