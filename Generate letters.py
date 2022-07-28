s = input()
row_1=''
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        row_1=s[:i]
        break
    else:
        row_1=s[:i+1]
row_2 = row_1[::-1]
print(row_1,row_2,sep='')
