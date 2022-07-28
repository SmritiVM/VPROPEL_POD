import itertools
d = input()
n = len(d)
k = int(input())
p = list(itertools.combinations(d,k))
for i in sorted(p):
    print(''.join(i))
    
'''d = list(input())
n = len(d)
k = int(input())

def n_length_combo(lst, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[i + 1:]
         
        for p in n_length_combo(remLst, n-1):
            l.append([m]+p)
             
    return l
       
comb = n_length_combo(d,k)
for i in sorted(comb):
    print(''.join(i))'''
