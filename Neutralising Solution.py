n = int(input())
c = list(map(int,input().split()))
for s in range(min(c),max(c)+1):
    b=0
    for i in range(n):
        c_new = s-c[i]
        b+=c_new
        
    if b==0:
        print("Yes")
        print(s)
        exit(0)

print("No")
