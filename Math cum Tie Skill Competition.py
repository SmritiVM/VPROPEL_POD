def form_string(num):
    s = ''
    while num>0:
        rem = num%3
        if rem==2:
            s+='b'
        elif rem==1:
            s+='g'
        else:
            s+='r'
        num//=3
    return s
    

def check_similarity(s1,s2,max_a):
    a=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            a+=1
        if a>max_a:
            return False
    if a==max_a:
        return True
    return False
    
def form_string_and_check(num,max_a):
    while True:
        check_s = form_string(num)
        if check_similarity(s,check_s,max_a):
            break
        num+=1
    return num
    
n = int(input())
s = form_string(n)
p = form_string_and_check(n+1,1)
q = form_string_and_check(n+1,2)


print(p,q,sep='\t')
length = 20-len(s)
s = s+'r'*length 
s1 = form_string(p)+'r'*length
s2 = form_string(q)+'r'*length
print(s[::-1])
print(s1[::-1])
print(s2[::-1])
