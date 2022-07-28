n1=input()
n2=input()
rmds=''
dig = ''
ind =2
while ind>=0:
    dig=str(int(n1[ind])+int(n2[ind]))
    print(dig)
    rmds+=dig[-1]
    ind-=1
print(int(rmds))
