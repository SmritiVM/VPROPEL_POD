n1 = int(input())
l1 = []
for i in range(n1):
    l1.append(int(input()))
n2 = int(input())
l2 = []
for i in range(n2):
    l2.append(int(input()))

def facindex(ind,l):
    if l[ind]%(ind+1)==0:
        return True
    return False

l3 = []
index = 0
i = 0
while True:
    
    try:
        if facindex(i,l1):
            l3.insert(index,l1[i])
            index+=1
            
        if facindex(i,l2):
            l3.insert(index,l2[i])
            index+=1
    except:
        break
    
    i+=1

if len(l2)>len(l1):
    l1,l2=l2,l1

i+=1   
while i<len(l1):
    if l1[i]%(i+1)==0:
        l3.insert(index,l1[i])
        index+=1
    i+=1

for j in range(len(l3)):
    if facindex(j,l3):
        print(l3[j])
