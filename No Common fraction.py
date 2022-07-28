u = int(input())
l= int(input())

def factor(num):
    fac=[]
    if num!=1:
        for i in range(1,num+1):
            if num%i==0:
                fac.append(i)
    else:
        fac.append(1)
    return fac
    
def hcf_fun(num1,num2):
    cf=[]
    fac_1=factor(num1)
    fac_2=factor(num2)
    for i in fac_1:
        if i in fac_2:
            cf.append(i)
    hcf=max(cf)
    return hcf

ncf=[]
def ncf_fun(low,up):
    global ncf
    for i in range(low,up+1):
        if i!=1:
            if hcf_fun(low,i)==1:
                ncf.append(low/i)
    low+=1
    if low<up:
        ncf_fun(low,up)
        
ncf_fun(l,u)        
count=0
for i in ncf:
    if i>0.2 and i<0.6:
        count+=1
        
print(count)
