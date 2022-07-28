#Coloured Coin Game

import copy
n = int(input())
o_colours = input().split()
colours_p1 = copy.deepcopy(o_colours)
colours_p2 = copy.deepcopy(o_colours)
n1 = int(input())
p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))

for i in p1:
        
    if i==1:
        colours_p1 = copy.deepcopy(o_colours)
    elif i==2:
        colours_p1.insert(1,'r')
    elif i==3:
        for j in range(2,6):
            colours_p1.insert(j,'r')
    elif i==4:
        colours_p1.pop(3)
    elif i==5:
        colours_p1.pop(4)
        colours_p1.pop(4)
    elif i==6:
        colours_p1.clear()
        
    
if colours_p1:
    print(*colours_p1,'')
else:
    print("No coins with player1")

for i in p2:
        
    if i==1:
        colours_p2 = copy.deepcopy(o_colours)
    elif i==2:
        colours_p2.insert(1,'r')
    elif i==3:
        for j in range(2,6):
            colours_p2.insert(j,'r')
    elif i==4:
        colours_p2.pop(3)
    elif i==5:
        colours_p2.pop(4)
        colours_p2.pop(4)
    elif i==6:
        colours_p2.clear()
if colours_p2:
    print(*colours_p2,'')
else:
    print("No coins with player2")
