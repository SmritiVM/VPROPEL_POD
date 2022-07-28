n = int(input())
r = []
for i in range(n):
    r.append(int(input()))
won = []
for i in range(len(r)):
    if i==0:
        if r[n-1]<r[0]<r[1]:
            won.append([r[i],i])
    elif i==n-1:
        if r[n-2]<r[n-1]<r[0]:
            won.append([r[i],i])
    else:
        if r[i-1]<r[i]<r[i+1]:
            won.append([r[i],i])
            
if won:
    for i in won:
        print(i[1]+1)
else:
    print(None)