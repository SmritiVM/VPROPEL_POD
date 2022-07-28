n = int(input())
m = int(input())
second = m+1
l=[]
while True:
    for i in range(1,n+1,2):
        for j in range(i,n+1,2):
            if m<i and i<j and m+i+j==n:
                line=[m,i,j]
                second = i
                l.append(line)
                
    m+=2
    if m>second:
        break

for line in l:
    for num in line:
        print(num,end=' ')
    print()
