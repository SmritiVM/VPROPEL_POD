from itertools import permutations 
seq = input()
name = input()
q = len(name)
pos = []
for i in range(len(seq)-q+1):
    section = seq[i:i+q]
    arrangements = list(permutations(section,q))
    for a in arrangements:
        if ''.join(a)==name:
            if i+1 not in pos:
                pos.append(i+1)

for i in pos:
    print(i)
