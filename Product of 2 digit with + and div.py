m,n = int(input()),int(input())
if m>n:m,n=n,m
line_1 = []
while m>=1:
    line_1.append(m)
    m//=2
line_1.sort()
#print(line_1)
line_2 = [n]
for i in range(1,len(line_1)):
    line_2.append(line_2[i-1]*2)
#print(line_2)
line_2.sort(reverse=True)
pdt = 0
for x,y in zip(line_1,line_2):
    if x%2!=0:
        print(x,y)
        pdt+=y
print(pdt)
