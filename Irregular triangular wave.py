
n = int(input())
number = list(map(int,input().split()))
for i in range(n):
    try:
        if i%2:
            if number[i]<number[i-1]:
                number[i-1],number[i]=number[i],number[i-1]
            elif number[i]<number[i+1]:
                number[i+1],number[i]=number[i],number[i+1]
        else:
            if number[i]>number[i+1]:
                number[i+1],number[i]=number[i],number[i+1]
            elif number[i]>number[i-1]:
                number[i-1],number[i]=number[i],number[i-1]
    except:
        continue
print(*number)
