medals = list(map(int,input().split()))
medals.pop()
n = int(input())
for i in range(len(medals)-1,0,-n):
    print(*medals[i-n+1:i+1],end=' ')

###Alt..Uttam's mthd
l = input().split()[:-1][::-1]
n=int(input())
print(*[" ".join(l[i : i + n][::-1]) for i in range(0,len(l),n)])
