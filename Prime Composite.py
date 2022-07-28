n = int(input())
m1 = (n-1)/6
print(m1)
m2 = (n+1)/6
print(m2)
print(m1-int(m1))
print(m2-int(m2))
if m1-int(m1)==0.0 or m2-int(m2)==0.0:
    print("Composite number")
else:
    print("Cannot be decided")
