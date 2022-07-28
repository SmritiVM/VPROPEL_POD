n = int(input())
def sod(n):
    sum = 0
    while n>0:
        dig=n%10
        sum+=(dig)**2
        n//=10
    return sum
c = 0
while n>=10:
    n=sod(n)
    c+=1
    print(n,c)
if n==4 and c<=10:
    print(c)
else:
    print('No')
        
