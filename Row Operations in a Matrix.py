m,n = map(int,input().split())
matrix = []
for i in range(m):
    matrix.append(list(map(int,input().split())))
    
c = int(input())
i = int(input())
def add_row(i,matrix):
    row = list(map(int,input().split()))
    matrix.insert(i-1,row)
    
def remove(i,matrix):
    matrix.pop(i-1)
    
def add_up(i,matrix):
    return sum(matrix[i-1])
    
def even(i,matrix):
    count = 0
    for ele in matrix[i-1]:
        if not i%2: count+=1
    return count
    
if c==1:
    add_row(i,matrix)
    for row in matrix:
        for ele in row:
            print(ele,end=' ')
        print()
    
elif c==2:
    remove(i,matrix)
    for row in matrix:
        for ele in row:
            print(ele,end=' ')
        print()
        
elif c==3:
    print(add_up(i,matrix))
    
else:
    print(even(i,matrix))
