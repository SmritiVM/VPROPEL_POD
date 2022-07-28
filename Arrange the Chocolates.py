n = int(input())
choco = list(map(int,input().split()))
pairs = []
sum_of_diff=0
choco.sort()
for i in range(0,n//2):
    pair = [choco[i],choco[n-i-1]]
    pairs.extend(pair)
    sum_of_diff+=abs(choco[i]-choco[n-i-1])

print(*pairs)
print(sum_of_diff)
