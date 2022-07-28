text = input()
vowels = ['a','e','i','o','u']
words = text.split()
def check(word,vowels):
    unique = []
    ind = 0
    flag = True
    for i in range(len(word)):
        if word[i] in vowels:
            if word[i] not in unique:
                unique.append(word[i])
            ind2 = vowels.index(word[i])
            if ind2<ind:
                flag = False
                break
            elif ind2>ind:
                ind = ind2
    if flag:
        return len(unique)
    else:
        return 0

lengths = {}     
for word in words:
    lengths[word]=check(word,vowels)
    
for word in lengths:
    if lengths[word]==max(list(lengths.values())):
        print(word)
