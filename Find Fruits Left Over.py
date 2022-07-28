s = list(input())

while True:
    n = len(s)
    for i in range(n-2):
        if s[i]!=s[i+1]!=s[i+2] and s[i]!=s[i+2]: 
            s=s[:i]+s[i+3:]
            break
    if len(s)==0 or len(list(set(s)))<3:
        break
if s:
    print("".join(s))
else:
    print('No fruit is left over')
