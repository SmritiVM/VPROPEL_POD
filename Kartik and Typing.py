n = int(input())#no. of words
words = []
let = {'d':'left','f':'left','j':'right','k':'right'}
count = 0
for i in range(n):
    count = 2
    word = input()
    for i in range(1,len(word)):
        if let[word[i-1]]==let[word[i]]:
            count+=4
        else:
            count+=2
            
    flag = True
    for i in words:
        if i[0]==word:
            words.append([word,i[1]//2])
            flag = False
            break
    if flag:
        words.append([word,count])
    
val = sum([x[1] for x in words])
print(val)
