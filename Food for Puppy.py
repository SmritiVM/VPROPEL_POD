n=int(input())
r=float(input())
for i in range(5):
    n+=n*r
    print(n)
print(format(n,'0.2f'))
