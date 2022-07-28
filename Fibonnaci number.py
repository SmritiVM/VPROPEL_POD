n = input()
F=set()
l = list(n)
for i in range(1,len(n)+1):
    f = set()
    for j in range(len(l)):
        ele = int("".join(l[j:j+i]))
        a = (5*ele*ele+4)**(0.5)
        b = (5*ele*ele-4)**(0.5)
        if a-int(a)==0 or b-int(b)==0:
            f.add(ele)
    F.update(f)
        
print(F)
