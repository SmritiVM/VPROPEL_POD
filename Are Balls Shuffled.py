n = int(input())
ball = []
for i in range(n):
    ball.append(input())

ball2 = []

for i in range(n):
    ball2.append(input())

def ball_rotate(ball,ball2,t,n):
    
    if ball==ball2:
        print('Not Shuffled')
        return 
    if t==n-1:
        print('Shuffled')
        return
    first= ball2[0]
    for i in range(n-1):
        ball2[i]=ball2[i+1]
    ball2[-1]=first
    t+=1
    ball_rotate(ball,ball2,t,n)
ball_rotate(ball,ball2,0,n)
    
