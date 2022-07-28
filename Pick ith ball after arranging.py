n = int(input())
balls = []
for i in range(n):
    rad,colour=input().split()
    balls.append([int(rad),colour])
balls.sort()
i = int(input())
print(*balls[i-1])
