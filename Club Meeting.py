m = int(input())
n = int(input())
for i in range(1,m*n+1):
    if i%m==0 and i%n==0:
        lcm=i
        break
print(lcm)
count = 0
d =1
while d<32:
    count+=1
    d+=lcm
print(count)
