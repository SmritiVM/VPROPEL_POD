n = int(input())
tkno_list=[]
for i in range(n):
    tk = input()
    tkno_list.append(tk)
    
family=[]
for i in range(n-1):
    p = input()
    c= input()
    pr_ch=[p,c]
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
        porc=''
        if int(j)!=2:
            for k in range(2,int(j)):
                if int(j)%k==0:
                    porc='comp'
                    break
                else:
                    porc='prime'
            if porc=='prime':
                prime.append(j)
        else:
            prime.append(j)
    print(prime)
    print(len(prime))

    
