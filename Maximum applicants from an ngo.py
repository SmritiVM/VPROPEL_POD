k = int(input())
m = int(input())
noa = list(map(int,input().split()))
dist_noa = sorted(list(set(noa)),reverse=True)
count = sum(dist_noa)
ngo = len(dist_noa)
count+=ngo

for i in set(noa):
    noa.remove(i)
    if (noa.count(i)-i-1)<=0:
        dist_noa.remove(i)
        
for i in dist_noa:
    dist_ngo = (noa.count(i)-i-1)
    if dist_ngo<=0 and k>ngo:
        count+=(i+1)
    elif k>ngo and (ngo+dist_ngo)<=k:
        count+=dist_ngo*(i+1)
    else:
        count+=(k-ngo)*(i+1)
        ngo+=dist_ngo
        break
    ngo+=dist_ngo
    
if k>ngo:
    count+=(k-ngo)*(max(noa)+1)
    
print(count)

