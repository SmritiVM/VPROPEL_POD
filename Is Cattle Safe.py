d = int(input())
x,y = map(float, input().split())
l=b=0
for i in range(d):
    for j in range(i+1,d):
        if i*i+j*j==d*d:
            l=i
            b=j

if b-x<=1 or l-y<=1 :
    print("Unsafe")
else:
    print("Safe")
