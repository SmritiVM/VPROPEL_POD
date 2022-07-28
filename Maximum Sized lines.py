n = int(input())
points=[]
for i in range(n):
    p = input()
    point=tuple(p.split())
    points.append(point)
hor=[]
ver=[]

def horver(p1,p2):
    global hor,ver
    if p1[0]==p2[0]:
        if p1 not in ver:
            ver.append(p1)
        if p2 not in ver:
            ver.append(p2)

    if p1[1]==p2[1]:
        if p1 not in hor:
            hor.append(p1)
        if p2 not in hor:
            hor.append(p2)
    
for i in range(len(points)):
    for j in range(len(points)):
        if i!=j:
            horver(points[i],points[j])

def maz(l):
    if len(l)!=0:
        return len(l)-1
    else:
        return 0
maz_hor=maz(hor)
maz_ver=maz(ver)

print(maz_hor)
print(maz_ver)
            

    
    
