p = int(input())
s = int(input())
n = int(input())
i = 1
water = 0
while i<=n:
    if i%2!=0:
        
        if i!=1:
            p+=s
        water += p
    i+=1
print(p)
print(water)
