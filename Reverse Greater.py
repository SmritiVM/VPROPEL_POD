s1,s2 = input().split(),input().split()
def word_greater(w1,w2):
    if len(w1)>len(w2) or (len(w1)==len(w2) and w1>w2):
        return True
    return False

n = len(s1)
for i in range(n):
    if word_greater(s1[i],s2[n-i-1]):
        continue
    else:
        print('No')
        exit(0)
print('Yes')
