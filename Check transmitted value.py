import math
r = int(input())
x = int(input())
n = int(input())
c = n^x
a=(r^x)/n
print(a)
if r==c:
    print("Correct transmission")

elif r>c:
    m = math.log(a)/math.log(2)
    print('Shifted left by',m,'bits')
else:
    m = -math.log(a)/math.log(2)
    print('Shifted right by',m,'bits')
