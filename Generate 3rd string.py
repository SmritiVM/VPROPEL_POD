s1 = input()
s2 = input()
#print(ord('Z'),ord('A'))
s3 = ''
for i in range(len(s1)):
    d = abs(ord(s1[i])-ord(s2[i]))
    new_d = ord(s2[i])+d
    if new_d>90:
        new_d-=26
    s3+=chr(new_d)
print(s3)
