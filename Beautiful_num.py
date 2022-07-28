import itertools
n = int(input())
ans =-1
for i in range(1,len(str(n))+1):
    for j in (int("".join(k)) for k in itertools.product('89',repeat=i)):
        if n%j==0:
            ans = 'beautiful'
            break
print(ans)
