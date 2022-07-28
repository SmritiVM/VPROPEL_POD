n = int(input()) #no. of nuts
m = int(input()) #no. of packages
nuts = list(map(int,input().split()))
combo = ''
flag = True

i=1
while i<=m:
    for x in nuts:
        if x==n:
            print(x)
            break
    
    nuts = [nuts[j]+nuts[j+1] for j in range(len(nuts)-1)]
    print(nuts)
    i+=1
        
