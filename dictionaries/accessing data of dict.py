a={'the':3,'a':5,10000:'value','dict':{3:4},'li':[1.2,3]}
#accessing data of dictionaries
print(a['the'])
'''print(a[key]) are used as indices , cant use 0,1,2... as index'''
print(a.get('a'))
print(a.get('o'))
print(a.get('ki',-1))
'''accessing value through sq bracket and get method is very similar
but if we try to access a key which is not present in dict then sqaure 
bracket will return an error while get method will return None as default'''

#getting keys,values of dictionary
print(a.keys())
print(a.values())
print(a.items())

#printing keys,values in a for loop
for i in a:
    print(i,a[i])
for i in a.values():
    print(i)

#checking if certain keys exist in dictionary (cant check values using this)
print('list' in a)
print(2 in a)
print('dict' in a)
