n = int(input())
sentences = [input().split() for i in range(n)]
for s in sentences:
    if all([s[i]>s[i+1] for i in range(len(s)-1)]) or all([s[i]<s[i+1] for i in range(len(s)-1)]):
        print(" ".join(s))
