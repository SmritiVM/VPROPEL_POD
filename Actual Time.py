x = int(input())
h = int(input())
m = int(input())
increment = 0
original_hour = 0
while True:
    original_hour+=1
    increment+=x
    if original_hour+increment//60==h and increment%60==m:
        print(original_hour)
        exit(0)
