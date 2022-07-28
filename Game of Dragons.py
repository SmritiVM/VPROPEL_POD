import itertools
s,n = tuple(map(int,input().split()))
xy_list=[]

for i in range(n):
    x,y = tuple(map(int,input().split()))
    xy_list.append([x,y])
    
p = list(itertools.permutations(xy_list))
trials=[]
def fight(trial):
    global s,trials
    ans = 'YES'
    for round in trial:
        if round[0]<s:
            s+=round[1]
        else:
            ans = 'NO'
            break

    trials.append(ans)
    
for trial in p:
    fight(trial)
    
if 'YES' in trials:
    print('YES')
else:
    print('NO')
