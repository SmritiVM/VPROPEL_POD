import string
n = int(input())
m = int(input())
pdt = n*m
l = list(str(n)+str(m)+str(pdt))

dig = string.digits
for i in dig:
    if i not in l or l.count(i)!=1:
        print('No')
        break
else:
    print('Yes')
