n = int(input())
matrix = [list(map(int,input().split())) for i in range(n)]
nums = [matrix[i][j] for i in range(n) for j in range(n)]
nums.remove(-1)
nums.sort()
for i in range(n):
    for j in range(n):
        if matrix[i][j]!=-1:
            pos = nums.index(matrix[i][j])
            corr_row = pos//n
            corr_column = pos%n
            print(matrix[i][j],abs((corr_row-i)*2)+abs(corr_column-j),sep='\t')

