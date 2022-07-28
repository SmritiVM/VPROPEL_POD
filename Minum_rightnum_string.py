def wait_add(n,list,s):
    if len(list)==0 or list[0]=='(':
        list.insert(0,n)
        print(list)
    elif list[0]<n:
        list.insert(0,n)
        print(list)
    else:
       s+=list[0]
       print(s)
       list.pop(0)
       print(list)
       wait_add(n,list,s)
    return s

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
            
m=input()
r=''
wait_stream=[]
for i in m:
    if i.isalpha():
        r+=i
    elif i.isdigit():
        r = wait_add(i,wait_stream,r)
    elif i=='(':
        wait_stream.insert(0,i)
    elif i==')':
        l2,wait_stream=leftpara(wait_stream)
        for i in ('(',')'):
            if i in wait_stream:                
                wait_stream.remove(i)
        for i in l2:
            r+=i
        print(l2)
        print(wait_stream)
    print(r)
                


for i in wait_stream:
    r+=str(i)
print(r)

################################################
#Alt soln
m = input()

def waiting_add(i,wait_stream,r):
    if not wait_stream or wait_stream[-1]=='(':
        wait_stream.append(i)
    elif int(i)>int(wait_stream[-1]):
        wait_stream.append(i)
    else:
        r+=wait_stream.pop()
        waiting_add(i,wait_stream,r)
    return r

wait_stream = []
r=''
for i in m:
    if i.isalpha():
        r+=i
    elif i.isdigit():
        r=waiting_add(i,wait_stream,r)
    elif i=='(':
        wait_stream+=i
    else:
        while wait_stream[-1]!='(':
            r+=wait_stream.pop()
        for i in ('(',')'):
            if i in wait_stream:                
                wait_stream.remove(i)
if wait_stream:
    r+=''.join(wait_stream[-1::-1])
print(r)
