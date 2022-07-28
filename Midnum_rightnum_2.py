m = input()
r=""
w=[]

def leftpara(list):
    l2=[]
    for i in list:
        if i=='(':
            break
        else:
            l2.append(i)
    for i in l2:
        if i in list:
            list.remove(i)
    return l2,list


for ch in m:
    if ch.isalpha():
        r+=ch
    elif ch=='(':
        w.insert(0,ch)
    elif ch==')':
        l2,w=leftpara(w)
        for i in l2:
            r+=i
        w.remove('(')
        w.remove(')')
    elif ch.isdigit() and w[0].isdigit() and int(w[0])>=int(ch):
        l3=[]
        for i in range(len(w)):
            if int(w[0])<int(ch) or w[0]=='(' or w[0]=='':
                break
            else:
                l3.append(i)
        for i in l3:
            r+=i
            w.remove(i)
    while w!=[]:
        for i in w:
            r+=i
            w.remove(i)
print(r)
            
                
        
