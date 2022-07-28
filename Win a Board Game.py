p = int(input()) #pXp dimension

m,n = map(int,input().split()) #Starting cell
num1 = int(input()) #no. of moves
moves = []
for i in range(num1):
    moves.append(input())
    
m1,n1 = map(int,input().split()) #Winning cell

pointer = [m,n]

for move in moves:
    m,n = pointer[0],pointer[1]
    if move=='l':
        if n>0:
            pointer = [m,n-1]
    elif move=='r':
        if n<p-1:
            pointer = [m,n+1]
    elif move=='u':
        if m<p-1:
            pointer = [m+1,n]
    elif move=='d':
        if m>0:
            pointer = [m-1,n]

if pointer==[m1,n1]:
    print('Win')
else:
    print('Loss')
