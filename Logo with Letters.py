r = int(input())
c = int(input())
matrix = []
mat_2=[]
for i in range(r):
    row = input().split()
    matrix.append(row)
    mat_2.extend(row)
if sorted(set(mat_2))==['l','x','z']:
    l_count = 0
    for i in range(r-1):
        for j in range(c-1):
            if matrix[i][j]=='l':
                if matrix[i+1][j]==matrix[i+1][j+1]=='l':
                    l_count+=1
        
    print(l_count)
else:
    print('Invalid')
