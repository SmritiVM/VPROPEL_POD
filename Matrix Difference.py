r1 = int(input())
c1 = int(input())
m1 = []
for i in range(r1):
    m1.append(list(map(int,input().split())))
r2 = int(input())
c2 = int(input())
m2 =[]
for i in range(r2):
    m2.append(list(map(int,input().split())))

m3 = m1
for i in range(r1):
    for j in range(c1):
        for row in m2:
            if m1[i][j] in row:
                m3[i][j]=0

print(m3)
