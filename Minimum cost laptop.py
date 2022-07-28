x = int(input())
n = int(input())
max_area=length=breadth=cost= 0
flag = True
for i in range(n):
    l,b,c = map(int,input().split())
    area = l*b
    if c<=x and area>max_area:
        max_area,length,breadth,cost = area,l,b,c
        flag = False
if flag:
    print('No laptop')
else:
    print(length, breadth, cost)
