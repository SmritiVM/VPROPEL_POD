n,m=map(int,input().split())
matrix = []
for i in range(n):
    row = list(input())
    matrix.append(row)

people =[]
for i in range(n):
    for j in range(m):
        if int(matrix[i][j])==1:
            people.append((i,j))
        

q = int(input())
for i in range(q):
    d = int(input())
    count = 0
    for i in range(len(people)):
        for j in range(i,len(people)):
            if (abs(people[i][0]-people[j][0])+abs(people[i][1]-people[j][1]))==d:
                count+=1
    print(count)
            
