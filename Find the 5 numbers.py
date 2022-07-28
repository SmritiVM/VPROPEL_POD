n= list(map(int,input().split()))
sum_abcde = sum(n)//4
c = sum_abcde-n[0]-n[9]
a = n[1]-c
b = n[0]-a
e = n[8]-c
d = n[9]-e
print(a,b,c,d,e)
