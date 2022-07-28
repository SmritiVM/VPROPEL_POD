n = int(input())
eve = [m for m in range(1,n+1) if m%2==0]
flag = True
for i in range(2,10**(7)+1):
    if all([i%m==0 for m in eve]):
        print(i)
        flag = False
        break
if flag:
    print('No such number in range')
