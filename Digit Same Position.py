n1 = input()
n2 = input()
n = len(n1)
posl=[]
for i in range(n):
    if n1[n-i-1]==n2[n-i-1]:
        posl.append(i)
print(posl)
for i in posl:
    pos = '1'+('0'*i)+'th'
    print("Same at",pos, "position")
