n = int(input())
m = int(input())
l=[]
for i in range(2,m+1):
    print(i)
    for j in range(10**(n-1),10**(n)):
        print(str(j)*2)
        if int(str(j)*2)%i!=0:
            break
    else:
        l.append(i)
        
        
if len(l)!=0:
    for i in l:
        print(i)
else:
    print('No complete factors')
