import math
s = input()
n = len(s)

for i in range(10**(n)-1,10**(n-1)-1,-1):
    if math.sqrt(i)-int(math.sqrt(i))==0:
        char = list(str(i))
        flag = len(set(char))==len(char)
        if flag:
            num = str(i)
            break
        

for i in range(n):
    print(s[i],num[i])

