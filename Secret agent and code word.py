s = input()
words = s.split()
def vowels_count(word):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in word:
        if i.lower() in vowels:
            count+=1
    return count
for i in range(len(words)):
    status = 0
    for j in range(len(words)):
        for k in words[i]:
            if i!=j and k in words[j] and words[i].count(k)==words[j].count(k) and vowels_count(words[i])==vowels_count(words[j]):
                status+=1
            
        if status==len(words[i]):
            print(words[i])
            break
