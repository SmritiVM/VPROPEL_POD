forward,backward = {},{}
j = 26
char = 'a'
for i in range(1,27):
    forward[i]=char
    backward[j]=char
    j-=1
    char = chr(ord(char)+1)

s1, s2 = input()[::-1],input()[::-1]
s3 = ''
i = 0
while i<len(s2):
    d = ord(s1[i])-ord(s2[i])
    if d==0:
        s3+=s1[i]
    elif d>0:
        s3+=forward[d]
    else:
        s3+=backward[abs(d)]
    i+=1
diff = len(s1)-len(s2)
print(s1[::-1][:diff]+s3[::-1])
