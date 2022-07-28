m = int(input())
c = int(input())
l = []
ind=1
round_ = 1
while ind<c+1:
    row = [0]*m
    if round_%2!=0:
        for i in range(m):
            row[i]=ind
            ind+=1
        l.append(row)
    else:
        for i in range(m-2,-1,-1):
            row[i]=ind
            ind+=1
        row[-1]=ind
        ind+=1
        l.append(row)
    round_+=1
for row in l:
    for i in range(m):
        if row[i]==c:
            print('S'+str(i+1))
            exit()
