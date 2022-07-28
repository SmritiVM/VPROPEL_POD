#Memoization
q = int(input())
dictFiboCache = {}
def fiboUsingCache(n):
    if n in dictFiboCache:
        return dictFiboCache[n]
    if n==1:
        value=1
    elif n==2:
        value=2
    elif n>2:
        value= fiboUsingCache(n-1) + fiboUsingCache(n-2)
    dictFiboCache[n]=value
    return value

for x in range(q):
    n = int(input())
    print(fiboUsingCache(n)%(10**9+7))
