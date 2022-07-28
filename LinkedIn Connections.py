'''n = int(input())#no. of people
m = int(input())#no. of connections
cons = {}

def checkins(d,n1,n2):
    if n1 not in d:
        d[n1]=[n2]
    else:
        d[n1].append(n2)
        
for i in range(m):
    n1,n2 = map(int,input().split())
    checkins(cons,n1,n2)
print(cons)'''    

cons = {1: [2, 5, 7, 9], 2: [4], 5: [3, 6], 7: [8, 10], 9: [10], 10: [11], 11: [12], 4: [6]}
    
k = int(input())#person who wants to send request
q = int(input())#no. of queries

def find_path(graph,start,end,path=[]):
    path = path + [start]
    if start==end:
        return path
    if not start in graph.keys():
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph,node,end,path)
        if newpath:
            if not shortest or len(newpath)<len(shortest):
                shortest=newpath
    return shortest
        
        
        
        
            
queries=[]   
for i in range(q):
    l = int(input())#person request should be sent to
    queries.append(l)

def checknone(path):
    if path==None:
        return True
def checklen(path):
    if (len(path)-1)<=3:
        print('yes')
    else:
        print('no')
    
for l in queries:
    path1 = find_path(cons,k,l)
    path2 = find_path(cons,l,k)
    print(path1,path2)
    if checknone(path1) and checknone(path2):
        print('no')
    elif checknone(path2):
        checklen(path1)
    elif checknone(path1):
        checklen(path2)
        
    else:
        if len(path1)>len(path2):
            path1,path2=path2,path1
        checklen(path1)
'''n,m=int(input()),int(input())
connect=[list(map(int,input().split())) for i in range(m)]
k=int(input())
tree=[[k],[],[],[]]
s=set([k])
for i in range(3):
    for j in connect:
        for y in tree[i]:
            if y in j:
                other=(j[0] if j[1]==y else j[1])
                if other not in s:
                    tree[i+1].append(other)
                    s.add(other)
q=int(input())
for i in range(q):
    per=int(input())
    for i in tree:
        if per in i:
            print('yes')
            break
    else:
        print('no')'''    

'''n=int(input())
m =int(input())
con = []
for i in range(m):
con.append(list(map(int,input().split())))
k=int(input())
graph=[[k],[],[],[]]
s=set([k])
for i in range(3):
    for j in con:
        for y in graph[i]:
            if y in j:
                
                if j[1]==y:
                    other=j[0]
                else:
                    other=j[1]
                if other not in s:
                    tree[i+1].append(other)
                    s.add(other)'''
'''q=int(input())
for i in range(q):
    per=int(input())
    for i in tree:
        if per in i:
            print('yes')
            break
    else:
        print('no')''' 
