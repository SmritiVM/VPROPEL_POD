n = int(input())
for i in range(n):
    x,y,z = map(int,input().split())
    count = 0
    while z>=x:
        z=z-2*x/3
        count+=1
    if round(z)==x: count+=1
    print(y*count)
