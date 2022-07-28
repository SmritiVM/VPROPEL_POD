n = int(input()) #no.of rows/columns

m = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    m.append(row)

bord = [] #elements in the border of matrix

#Collecting border elements
#first row
for j in range(0,n):
    bord.append(m[0][j])

#last column
for i in range(1,n):
    bord.append(m[i][n-1])

#last row
for j in range(n-2,-1,-1):
    bord.append(m[n-1][j])

#first column
for i in range(n-2,0,-1):
    bord.append(m[i][0])


#Swapping
for i in range(2,len(bord),2):
    bord[i],bord[i-2]=bord[i-2],bord[i]

#Repacing border elements
ind = 0
#first row
for j in range(0,n):
    m[0][j]=bord[ind]
    ind+=1

#last column
for i in range(1,n):
    m[i][n-1]=bord[ind]
    ind+=1

#last row
for j in range(n-2,-1,-1):
    m[n-1][j]=bord[ind]
    ind+=1

#first column
for i in range(n-2,0,-1):
    m[i][0]=bord[ind]
    ind+=1

#Printing answer
for row in m:
    for ele in row:
        print(ele,end='\t')
    print()

    
