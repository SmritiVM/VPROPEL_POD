import re
word = input().lower()
pattern = r"([a-z])\1+"
while re.search(pattern,word):
    word=re.sub(pattern,'',word)
   
print(1 if word=='' else 0)

#Alt code
from itertools import groupby
def strconv(m):
    s=''
    for i in m:
        s+=i
    k = [''.join(g) for a,g in groupby(s)] 
    return k

def iterate(l):
    i=0
    while(i<len(l)):
        if (l[i]=='*'):
            l.pop(i)
        elif (len(l[i])>1):
            l[i]='*'
        i+=1
        l = strconv(l)
    return l

s = input().lower()
n = [''.join(g) for a,g in groupby(s)]
m = len(n)
i = 0
while(i<m):
    n = iterate(n)
    print(n)
    i+=1
if(n==['*']):
    print(l)