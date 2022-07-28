import string
s1 = input()
s2 = input()
def stepped(s1,s2):
    if len(s1)!=len(s2):
        return 'Length different'
    
    for i in string.punctuation:
        if i in s1 or i in s2:
            return 'Strings contain non alphabets'
            
    for i in string.digits:
        if i in s1 or i in s2:
           return 'Strings contain non alphabets' 
    flag = True
    pos=s1.find(' ')
    for i in range(pos,len(s1)):
        if s1[i].isspace() and s2[i]!=' ':
            flag = False
            return 'Strings differ in space'
    
        
    s = list(string.ascii_lowercase)
    a = [x for x in range(1,27)]
    d = {}
    for i in range(len(s)):
        d[s[i]]=a[i]
    flag = True
    count = 1
    for i in range(len(s1)):
        if s1[i]!= ' ':
            if (abs(d[s1[i]]-d[s2[i]])==count):
                count+=1
            else:
                flag = False
                return 'Strings are not stepped'
    if flag:
        return 'Strings are stepped'
print(stepped(s1,s2))
