n = int(input())
a = int(input())
b = int(input())
n1,n3=a,b
if n1<n3:
    n1,n3=n3,n1
n2= n-(n1+n3)
if n1>=n2>=n3:
    print(n1,n2,n3)
else:
    print('Cannot be written')
