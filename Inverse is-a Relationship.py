n = int(input())
tree = {}
for i in range(n):
    m = int(input())
    for j in range(m):
        parent,child = input().split()
        if not parent in tree:
            tree[parent]=[child]
        else:
            tree[parent].append(child)

query = input()
print(*tree[query])
