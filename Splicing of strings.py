s1 = input()
s2 = input()
def duplicate(s):
    l=list(s)
    l2=l
    l2.reverse()
    for i in l:
        if l.count(i)>1:
            l2.remove(i)

    l2.reverse()
    return l2
            

l1 = duplicate(s1)
l2 = duplicate(s2)
s11=s22=''
for i in l1:
    s11+=i
for i in l2:
    s22+=i
s1,s2=s11,s22

splice=[]

def crossover(s1,s2,char):
    global splice
    t1 = s1.partition(char)
    t2 = s2.partition(char)
    S1 = t1[0]+char+t2[2]
    S2 = t2[0]+char+t1[2]
    splice.append(S1)
    splice.append(S2)

char=[]
for i in s1:
    if i in s2:
        char.append(i)

for i in char:
    crossover(s1,s2,i)


    
            
            
