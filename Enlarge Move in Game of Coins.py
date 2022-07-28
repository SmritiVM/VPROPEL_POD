import copy
r,c = int(input()),int(input())
matrix= []

for i in range(r):
    row = (list(map(int,input().split())))
    matrix.append(row)
    
    
matrix_transpose = [[matrix[j][i] for j in range(r)] for i in range(c)]
matrix_enlarged = copy.deepcopy(matrix)

for i in range(r):
    for j in range(c):
        max_r= max(matrix[i])
        min_c = min(matrix_transpose[j])
        matrix_enlarged[i][j]+=max_r+min_c

for row in matrix_enlarged:
    for ele in row:
        print(ele,end=' ')
    print()
    
