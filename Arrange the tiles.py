n = int(input())
curr = list(map(int,input().split()))
des = list(map(int,input().split()))
moves = 0
ind = 0
while curr!=des:
    for i in range(n):
        if curr[ind]==des[ind]:
            continue
        elif curr[i]==des[ind]:
            curr[ind],curr[i]=curr[i],curr[ind]
            moves+=1
            break
    ind+=1
    
print(moves)
