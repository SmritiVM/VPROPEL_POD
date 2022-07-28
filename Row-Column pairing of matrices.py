r1 = int(input())
c1 = int(input())
m1 =[]
for i in range(r1):
    m1.append(list(map(int,input().split())))
r2 = int(input())
c2 = int(input())
m2 = []
for i in range(r2):
    m2.append(list(map(int,input().split())))
m2 = [[m2[j][i] for j in range(r2)] for i in range(c2)]
s = int(input())

m3 = []
for i in range(r1):
    row = []
    for j in range(c1):
        count = 0
        l = list(zip(m1[i],m2[j]))
        for ele in l:
            if sum(ele)<=s:
                count+=1
        row.append(count)
    m3.append(row)
for i in range(r1):
    for j in range(c1):
        print(m3[i][j],end='\t')
    print()
