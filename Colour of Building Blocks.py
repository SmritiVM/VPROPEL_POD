n = int(input())
colours = input().split()
m =int(input())
seq = input()
ind = m
flag = False
colour_pos = {}
for i in colours:
    colour_pos[i]=[]
for i in range(len(seq)):
    colour_pos[seq[i]].append(i)

for i in colour_pos:
    for j in range(len(colour_pos[i])-1):
        if(abs(colour_pos[i][j]-colour_pos[i][j+1])<=m):
            flag = True
if flag:
    print("Invalid")
    
else:
    print("Valid")
