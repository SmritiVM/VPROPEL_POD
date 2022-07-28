from math import *
l,u = int(input()),int(input())
L = int(l**(1/3))
U = ceil(u**(1/3))
for i in range(L,U+1):
    if len(set(str(i)))==1:
        a = i**3
        if str(a)!=str(a)[::-1] and a>=l and a<=u and len(str(i))>1:
            print(a,i,sep='\t')
            
