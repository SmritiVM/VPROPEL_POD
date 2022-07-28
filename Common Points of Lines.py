com = []
n = int(input())
lines = []
for i in range(n):
    a,b,k = map(float,input().split())
    line = []
    while a<=b:
        line.append(a)
        a+=k
        a = round(a,1)
    lines.extend(line)

for point in sorted(lines):
    if lines.count(point)==n:
        if point not in com:
            if int(point)==point:
                com.append(int(point))
            else:
                com.append(point)
print(*com)
