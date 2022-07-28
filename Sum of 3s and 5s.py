n = int(input())
q=0
if n%3==0:
    print("Only three's")
elif n%5==0:
    print("Only five's")
else:
    while n%3!=0:
        n-=5
        q+=1
    p=n//3
    print(p,q)
