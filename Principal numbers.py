n = int(input())
col = [int(input()) for i in range(n)]

def largest_proper_factor(num):
    pf = 1
    for i in range(2,num):
        if num%i==0:
            if i>pf:
                pf = i
    return pf

new_col=[]    
for i in range(len(col)-1):
    l = [largest_proper_factor(col[x])<=largest_proper_factor(col[i]) for x in range(i+1,len(col))]
    if all(l):
        print(col[i])
        new_col.append(col[i])

if col[-1] not in new_col:
    print(col[-1])
