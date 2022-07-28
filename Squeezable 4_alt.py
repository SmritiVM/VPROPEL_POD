n = input()
c = 0
s = 0
while True:
    s = 0
    for i in n:
        s+=int(i)**2
    
    c+=1
    print(s,c)
    n = str(s)
    if s==4:
        break
    
print(c)
