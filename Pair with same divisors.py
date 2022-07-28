n = int(input())

def div(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count
    
def d(n):
    factors = []
    for i in range(1,n//2+1):
        if n%i==0 and i<n//i:
            factors.append((i,n//i))
    if not factors:
        return -1
    count=0
    for pair in factors:
        if div(pair[0])==div(pair[1]):
            count+=1
    return count
    
print(d(n))
