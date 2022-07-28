x = int(input())
if x%12==0:
    last = x//12
else:
    last = x//12 + 1
colours_num = {}
colours = ["Green","Orange","Blue","Blue","Orange","Green"]
num = 1
multiplier = 2
for i in range(last):
    for j in range(6):
        num2 = 6*multiplier+1-num
        colours_num[(num,num2)]=colours[j]
        num+=1
    num+=6
    multiplier+=4

for pair in colours_num:
    if x in pair:
        if x==pair[0]:
            print(pair[1])
        else:
            print(pair[0])
        print(colours_num[pair])
