elements={}
for i in range(2):
    elements[tuple(input().split())]=1
for i in range(2,8):
    for j in range(5):
        elements[tuple(input().split())]=i
period = int(input())
symbol = input()
#print(elements)
for i in elements:
    if i[1]==symbol:
        print(i[0],i[2],i[3],i[4],i[5])
