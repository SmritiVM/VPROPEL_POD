n = int(input())
points = list(map(int,input().split()))
up=dwn=0
i=1
upl = [points[0]]
down = []

while i<len(points):
    if points[i]>points[i-1]:
        if len(down)>0:
            dwn+=1
            down = []
        upl.append(points[i])
        
    elif points[i]<points[i-1]:
        if len(upl)>0:
            up+=1
            upl=[]
        down.append(points[i])
        
    i+=1
if len(upl)!=0:
    up+=1
if len(down)!=0:
    dwn+=1

print(up,dwn)
