n = int(input())
if n%2==0:
    y=(n+6)//2
    x=y-6
else:
    y=(n+7)//2
    x=y-7
print(x)
print(y)

##Alt mthd
n = int(input())
if n%2==0:
    max_pdt=(n//2)**2
    #xy = (n//2)**2-9..so we can fatorise like 
    x = n//2-3
    y = n//2+3
else:
    max_pdt=(n//2)(n//2+1)
    #xy = (n//2)**2 + n//2 -12
    x = n//2-3
    y=n//2+4
print(x+y)


##Alt mthd2
n = int(input())
print(n//2 - 3, n - (n//2 - 3), sep = '\n')
