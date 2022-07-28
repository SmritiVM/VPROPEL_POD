import math
b = int(input())
disc=0
if b>=5000:
    disc=25
elif 3000<=b<=4999:
    disc=15
elif 1000<=b<=2999:
    disc=10
else:
    disc=5
p= b-b*(disc/100)
dec=p-int(p)
D=0
if dec>=0.5:
    D=math.ceil(p)
else:
    D=math.floor(p)
print(D)
