n = int(input())
s1 = 0
s2 = 0
for i in range(n,0,-1):
    if s1<=s2:
        s1+=i
    else:
        s2+=i
print(abs(s1-s2))