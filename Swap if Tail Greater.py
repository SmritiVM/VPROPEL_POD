n = int(input())
col = [input() for i in range(n)]

def tailgreater(a,b,ind):
    try:
        if int(b[ind])>int(a[ind]):
            return True
        else:
            if int(b[ind])==int(a[ind]):
                return tailgreater(a,b,ind-1)
            else:
                return False
    except:
        return False
    return False
        
for i in range(len(col)-1):
    ind = -1
    if tailgreater(col[i],col[i+1],ind) is False:
        col[i],col[i+1]=col[i+1],col[i]
        
print(*col,sep='\n')
