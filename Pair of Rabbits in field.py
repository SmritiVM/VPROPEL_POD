def total_rabbits(n,m):
    f0 = f1 = n
    for i in range(m-1):
        f0,f1=f1,f0+f1
    return f0
n = int(input())
m = int(input())
for i in range(n,0,-1):
    rab_count= total_rabbits(i,m)
    if rab_count%3==0:
        print(i,rab_count)
        exit(0)
        
