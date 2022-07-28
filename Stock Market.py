d1,d2 = map(int,input().split())

def calc_stock(n,d1,d2):
    
    for i in range(3,n+1):
        d = d1*4+d2*3
        d1,d2=d2,d
    return d
q = int(input())
queries = list(map(int,input().split()))
res = []
for i in queries:
    if i>2:
        a = calc_stock(i,d1,d2)%(10**9+7)
        res.append(a)
    elif i==1:
        res.append(d1)
    elif i==2:
        res.append(d2)
print(*res)
    
