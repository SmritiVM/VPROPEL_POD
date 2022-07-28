def beautiful(n):
    l=[i for i in "8"*len(n)+"9"*len(n)]
    print(l)
    flag=0
    m=[]
    for i in range(len(l)+1):
        print(i)
        m+=[l[j:i] for j in range(i)]
        print(m)
        o=[''.join(i) for i in m if len(''.join(i))<=len(n)]
        print(o)
    for i in o:
        if int(n)%int(i)==0:
            flag=1
    if flag==1:
        return "beautiful"
    else:
        return -1
print(beautiful(input()))


