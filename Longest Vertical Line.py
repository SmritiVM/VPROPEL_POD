n = int(input())
points = [list(map(int,input().split())) for i in range(n)]
max_length = 0
fin_line = ()
fin_ycoords= ()
for i in range(n-1):
    temp_line = [points[i]]
    for j in range(i+1,n):
        if points[i][0]==points[j][0]:
            temp_line.append(points[j])
    y_coords = [x[1] for x in temp_line]
    d = max(y_coords)-min(y_coords)
    if d>max_length:
        max_length=d
        fin_line = tuple(temp_line)
        fin_ycoords = tuple(y_coords)
for p in fin_line:
    if p[1]==min(fin_ycoords):
        start = p
    if p[1]==max(fin_ycoords):
        end = p
print(*start)
print(*end)
print(max_length)
print(len(fin_line))
