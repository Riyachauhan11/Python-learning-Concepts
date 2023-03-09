'''Given a string S, you need to remove all the duplicates. 
That means, the output string should contain each character only once. 
The respective order of characters should remain same, as in the input string.

Sample Input 1 :

ababacd

Sample Output 1 :

abcd
'''

from collections import OrderedDict



def uniqueChar(s): 
    # Write your code here
    d=OrderedDict()
    for char in s:
        d[char]=d.get(char,0)+1
        
    uniq=''
    for char in d:
        uniq=uniq+char
    return uniq
    



# Main 
s=input() 
print(uniqueChar(s))
