n = int(input())
tree = {}
for i in range(n):
    parent,child = tuple(input().split())
    if child in tree:
        tree[child].append(parent)
    else:
        tree[child]=[parent]
for child in tree:
    for parent in tree[child]:
        if parent in tree:
            for relation in tree[parent]:
                if relation not in tree[child]: tree[child].append(relation)
node = input()
print(*tree[node])
