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

##Uttam's code
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
s = int(input())
for i in range(n):
    for j in range(n):
        if l[i][j] == -1:continue
        x = 2*abs(i - (l[i][j] - s)//n) + abs(j - (l[i][j] - s)%n)
        print(l[i][j],x,sep = '\t') 
