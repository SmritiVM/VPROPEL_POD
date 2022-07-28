n = int(input())
tk = input()
tkno_list=tk.split()
family=[]
for i in range(n-1):
    pc = input()
    pr_ch=pc.split()
    family.append(pr_ch)
    


def famchild(list,token):
    global tkno_list,child
    l2=[]
    for i in range(len(list)):
        if list[i][0]==token:
            l2.append(list[i][1])
            child.append(list[i][1])
    for i in tkno_list:
        if i in l2:
            famchild(list,i)
    
def primech(num):
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
                
q = int(input())
tkno_search=[]
for i in range(q):
    tkno=input()
    tkno_search.append(tkno)

for i in tkno_search:
    child=[]
    famchild(family,i)
    prime=[]

    for j in child:
        if primech(int(j))==True:
            prime.append(j)
    print(prime)
    print(len(prime))

    
