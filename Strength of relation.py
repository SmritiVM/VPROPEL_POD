n = int(input())
S = [input() for i in range(n)]
w = input()
def strength_of_relation(s1,s2):
    strength = sum([s1.find(c)*s2.find(c) for c in s1 if c in s2])
    return strength
max_strength = 0
word = []
for s in S:
    strength = strength_of_relation(s,w)
    if strength > max_strength:
        max_strength = strength
        word = [s]
    elif strength == max_strength:
        word.append(s)
print(*word,sep='\n')
