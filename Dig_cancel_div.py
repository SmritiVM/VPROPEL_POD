x = int(input())
y = int(input())

def dig_list(n):
    l=[]
    if n==0:
        l.append(n)
    else:
        while n>0:
            dig=n%10
            l.append(dig)
            n//=10
        l.reverse()
    return(l)

x_dig=dig_list(x)
y_dig=dig_list(y)
print(x_dig)
print(y_dig)

n1 = len(x_dig)
print(n1)

def com(a1,a2):
    for i in a1:
        if i in a2:
            a1.remove(i)
            a2.remove(i)
            com(a1,a2)
    return a1,a2


        
x_dig,y_dig=com(x_dig,y_dig)  

print(x_dig)
print(y_dig)
        
def isEmpty(list):
    if len(list)==0:
        list=[1]
    return list
    
x_dig=isEmpty(x_dig)
y_dig=isEmpty(y_dig)
print(x_dig)
print(y_dig)

def num(dig_list):
    dig_list.reverse()
    num=0
    for i in range(len(dig_list)):
        num+=dig_list[i]*10**i
    return num
    
x = num(x_dig)
y = num(y_dig)

if y==0:
    result = -1
else:
    result=x/y
    
print(format(result,'0.2f'))

########################################################
#Alt soln

x = int(input())
y = int(input())

x_dig=list(str(x))
y_dig=list(str(y))

def com(l1,l2):
    for i in l1:
        if i in l2:
            l1.remove(i)
            l2.remove(i)
            com(l1,l2)
    return l1,l2

def empty(l):
    if len(l)==0:
        l=['1']
    return l
x_dig,y_dig=com(x_dig,y_dig)
x_dig,y_dig=empty(x_dig),empty(y_dig)
x = int(''.join(x_dig))
y = int(''.join(y_dig))

if y!=0:
    result=x/y
else:
    result=-1
print(format(result,'0.2f'))
