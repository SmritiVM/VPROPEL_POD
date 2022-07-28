m = int(input())#no. of rows
n = int(input())#no. of columns
p = int(input())
q = int(input())
matrix = []
win_matrix=[]
for i in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)
l = int(input())#lucky no.

if l!=p:
    p,q=q,p



for i in range(m):
    row = []
    for j in range(n):
        column = [matrix[a][j] for a in range(m)]
        if matrix[i][j]==p:
            if (q in matrix[i]) or (q in column) :
                row.append(q)
            else:
                row.append(p)
        else:
            row.append(q)
    win_matrix.append(row)
                
winners=[]
for i in range(m):
    for j in range(n):
        if win_matrix[i][j]==p:
            winners.append((i+1,j+1))
            
if len(winners)>0:
    for i in winners:
        print(i[0],i[1])
else:
    print('No winner')
