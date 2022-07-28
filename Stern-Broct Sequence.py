n = int(input())
seq = list(map(int,input().split()))
flag = False
ind = 1
if seq[0]==seq[1]==1:
    for i in range(2,n):
        if i%2==0:
            if seq[i]==seq[i//2-1]+seq[i//2]:
                continue
            else:
                flag = True
                ind = i+1
                break
        else:
            if seq[i]==seq[i//2]:
                continue
            else:
                flag = True
                ind = i+1
                break
else:
    flag = True
if flag:
    print("No")
    print(ind)
else:
    print("Yes")
