n = int(input())
m = int(input())
child = {}
for i in range(n):
    entry = input().split()
    child[entry[0]] = entry[1:]
k = int(input())
for i in range(k):
    child1, child2 = tuple(input().split())
    child[child1],child[child2] = child[child2], child[child1]
    
for i in child:
    print(i, *child[i],'')
