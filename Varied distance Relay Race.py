from itertools import combinations
x = int(input())
n = int(input())
cap = list(map(int,input().split()))
for comb in list(combinations(enumerate(cap),4)):
    players = [t[1] for t in comb]
    indices = [t[0]+1 for t in comb]
    
    if sum(players)==x:
       print(*indices)
       exit(0)
print("No")
