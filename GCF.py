n1 = int(input())
n2 = int(input())
gcf = 0
if n1<n2:
    n1,n2=n2,n1
for i in range(1,n1):
    print(i)
    if n1%i==0 and n2%i==0:
        gcf = i
print(gcf)
if gcf==1:
    print('No')
else:
    print(gcf)
