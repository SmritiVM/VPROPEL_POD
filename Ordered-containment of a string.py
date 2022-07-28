s1=input()
s2=input()
n = len(s1)
ind = 0
ind2 =0
res=''
def find():
    global n,ind,ind2
    print(n,ind,ind2)
    for i in range(ind,n):
        
        if s2[ind2]==s1[i]:
            ind = i
            ind2+=1
            res='Yes'
            if ind2==len(s2):
                break
            else:
                find()
            
            
        else:
            res='No'
            
    return res
print(find())


#################################
#Alt soln and working one
s1=input()
s2=input()
l = []
pos = s1.find(s2[0])
flag = True
for i in range(pos,len(s1)-2):
    for j in range(i+1,len(s1)-1):
        for k in range(j+1,len(s1)):
            ele= s1[i]+s1[j]+s1[k]
            if ele==s2:
                flag = False
                break
if flag:
    print('No')
else:
    print('Yes')