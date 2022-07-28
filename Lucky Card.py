n = int(input())
m = int(input())
matrix = [input().split() for i in range(n)]
p = input()
flag = True
for row in matrix:
    if all([i in row for i in p]):
        print("".join(sorted(row)))
        print("Lucky Player")
        flag = False
        break
    
for i in range(m):
    column = []
    for j in range(n):
        column.append(matrix[j][i])
    if all([i in column for i in p]):
        print("".join(sorted(column)))
        print("Lucky Player")
        flag = False
        break

if flag:
    print("Unlucky Player")
           
       
