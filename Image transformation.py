#Image Transformation
n = int(input()) #no.of rows/columns

m = []
for i in range(n):
    row = list(map(int,input().split()))
    m.append(row)

if n%2!=0: #odd matrix
    for j in range(0,n,2): #first row swap
        try:
            m[0][j],m[0][j+2]=m[0][j+2],m[0][j]
        except:
            break

    for i in range(0,n,2): #last column swap
        try:
            m[i][n-1],m[i+2][n-1]=m[i+2][n-1],m[i][n-1]
        except:
            break

    for j in range(n-1,0,-2): #last row swap
        try:
            m[n-1][j],m[n-1][j-2]=m[n-1][j-2],m[n-1][j]
        except:
            break

    for i in range(n-1,0,-2): #first column swap
        if i-2==0:
            break
        else:
            try:
                m[i][0],m[i-2][0]=m[i-2][0],m[i][0]
            except:
                break


else: #even matrix
    for j in range(0,n,2): #first row swap
        try:
            m[0][j],m[0][j+2]=m[0][j+2],m[0][j]
        except:
            break

    m[0][n-2],m[1][n-1]=m[1][n-1],m[0][n-2] #bringing to last column

    for i in range(1,n,2): #last column swap
        try:
            m[i][n-1],m[i+2][n-1]=m[i+2][n-1],m[i][n-1]
        except:
            break

    for j in range(n-1,1,-2): #last row swap
        try:
            m[n-1][j],m[n-1][j-2]=m[n-1][j-2],m[n-1][j]
        except:
            break

    m[n-1][1],m[n-2][0]=m[n-2][0],m[n-1][1] #bringing to first column
    
    for i in range(n-2,0,-2): #first column swap
        if i-2==0:
            break
        else:
            try:
                m[i][0],m[i-2][0]=m[i-2][0],m[i][0]
            except:
                break

print(m)
