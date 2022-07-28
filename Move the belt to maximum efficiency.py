nuts,bolts = input(),input()
max_len = 0
ind = len(nuts)
def lcsubstr(str1, str2):
    ans = 0
    pos1=pos2=0
    for i in range(len(str1)):
        for j in range(len(str2)):
            k = 0
            while ((i + k) < len(str1) and (j + k) < len(str2) and str1[i + k] == str2[j + k]):
                k = k + 1
            if k > ans:
                ans = k
                pos1=i+1
                pos2=j
    return ans,pos1,pos2
length,pos1,pos2 = lcsubstr(nuts,bolts[::-1])
print(length,pos1,len(bolts)-pos2,sep='\n')

