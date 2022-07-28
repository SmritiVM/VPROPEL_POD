'''Note: Pvt test cases don't pass when gcd 1 is looked,
Question is wrong'''
u = int(input())
l = int(input())
count=0
L=[]
ncf=[]
for i in range(l,u+1):
    L.append(i)
print(L)
for i in range(len(L)):
    for j in range(i,len(L)):
        x = L[i]/L[j]
        if x not in ncf:
            ncf.append(L[i]/L[j])

for i in ncf:
    if i>0.2 and i<0.6:
        count+=1
print(count)

###########
#####Alt soln
upper = int(input())
lower = int(input())
ncfs = []
for i in range(lower,upper+1):
    for j in range(lower,upper+1):
        if i<j:
            frac = i/j
            if 0.2<frac<0.6 and (frac not in ncfs):
                ncfs.append(frac)
print(len(ncfs))