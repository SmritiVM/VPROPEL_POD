n = int(input())
s = [int(input()) for i in range(n)]
d = int(input())
xor = int(input())
n1,n2=0,0
for i in range(n):
    for j in range(i+1,n):
        if abs(s[i]-s[j])==d and s[i]^s[j]==xor:
            n1,n2=s[i],s[j]
            break
if n2<n1:
    n1,n2=n2,n1
print(n1,n2,sep='\t')
