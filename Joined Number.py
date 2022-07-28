n = input()
h = int(input())
for i in range(len(n)):
    for j in range(len(n)):
        num = n[i:j+1]
        if sum(list(map(int,num)))==h:
            print(num,end='\t')
