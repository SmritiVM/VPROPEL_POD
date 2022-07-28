n = int(input())
m = int(input())
b = bin(n)[2:]
print(b)
print(b[-m])
if b[-m]=='1':
    n=n>>(m-1)
else:
    n=n<<(m-1)
print(n)
