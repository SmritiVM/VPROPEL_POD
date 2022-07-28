n = int(input())
tkno_list=list(map(int, input().split()))
family=[]
res=[]
for i in range(n+1):
    family.append([])
    res.append(0)
for i in range(n-1):
    p,c=map(int,input().split())
    family[p].append[c]


def isPrime(num):
    if num<=0:
        return False
    if num==2:
        return True
    else:
        porc=''
        for i in range(2,num):
            if num%i==0:
                porc='comp'
                break
            else:
                porc='prime'
        if porc=='prime':
            return True

def traverse(parent):
    for child in family[parent]:
        traverse(child)
    for child in family[parent]:
        if(isPrime(tkno_list[child-1])):
            res[parent]+=1
        res[parent]+=res[child]

traverse(1)

q=int(input())
for i in range(q):
    x = int(input())
    print(res[x])

            
           
