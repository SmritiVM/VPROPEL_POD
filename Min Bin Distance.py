n = int(input())
c = [int(input()) for i in range(n)]
m = int(input())
def dist(n1,n2):
    d = 0
    if len(n2)>len(n1):
        n1,n2=n2,n1
    for i in range(len(n1)):
        try:
            if n1[i]==n2[i]:
                continue
            else:
                d+=1
        except:
            d+=1
    return d

min_dist = len(bin(max(c)))
ele = []
for num in c:
    n1 = bin(num)[2:][::-1]
    n2 = bin(m)[2:][::-1]
    distance = dist(n1,n2)
    if distance<min_dist:
        min_dist=distance
for num in c:
    n1 = bin(num)[2:][::-1]
    n2 = bin(m)[2:][::-1]
    distance = dist(n1,n2)
    if distance==min_dist:
        ele.append(num)
for i in ele:
    print(i)
    
