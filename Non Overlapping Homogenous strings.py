s = input()
k = int(input())
same_subs=[]
indices_visited = []
n = len(s)
for i in range(n):
    j = i+k
    sub = s[i:j]
    indices = [x for x in range(i,j)]
    if all([y not in indices_visited for y in indices]):
        if len(sub)==k and all([sub[k]==sub[0] for k in range(1,k)]):
            same_subs.append(sub)
            indices_visited.extend(indices)
print(len(same_subs))
