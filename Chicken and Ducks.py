n = int(input())
baskets = {}
for i in range(n):
    b = list(input().split())
    baskets[b[0]]=int(b[1])


basket_val = list(baskets.values()) 
m = len(basket_val)
ans =[]
flag = True

for i in range(m):
    if flag:
        for j in range(i+1,m):
            k = [x for x in basket_val if x!=basket_val[i] and x!=basket_val[j]]
            
            if 2*(basket_val[i]+basket_val[j])==sum(k):
                ans=[basket_val[i],basket_val[j]]
                ans.extend(k)
                flag=False
                break

            
ducks=[]
chickens=[]
for i in baskets:
    if baskets[i] in ans[0:2]:
        ducks.append(i)
    else:
        chickens.append(i)
        
print(ducks[0],ducks[1])
print(' '.join(chickens))
