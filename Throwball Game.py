m = int(input()) #max prize amt
n = int(input()) #no. of players
players = {}
for i in range(1,n+1):
    p = list(input().split())
    players[i]=[p[0],int(p[1])]
    
ind = int(input()) #index of player who caught first
x = input() #player to be found
count = 0
def find(x,players,ind,count):
    if players[ind][0]==x:
        return count
    else:
        count+=1
        return find(x,players,players[ind][1],count)
count = find(x,players,ind,count)
prize = m - (m*count*2/100)
print(format(prize,'0.2f'))
