n,k = map(int,input().split())
ticket_details = [list(map(int,input().split())) for i in range(n)]
max_points = 0
start = 0
for i in range(0,n-k+1):
    points = sum([x[1] for x in ticket_details[i:i+k])
    if points> max_points and len(group)==k: 
        max_points = points
        start = ticket_details[i][0]
print(start)
