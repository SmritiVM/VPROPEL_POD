import math
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if math.gcd(x,y)>1:
        print('IMPOSSIBLE')
    else:
        print((x-1)*(y-1))
