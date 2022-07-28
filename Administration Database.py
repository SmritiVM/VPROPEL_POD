from itertools import permutations
uin = input()
n = len(uin)
start = 1
flag = 1
while start<n:
    p= permutations(uin,start)
    for num in p:
        uin_temp = list(uin)
        for i in num:
            uin_temp.remove(i)
        if (int(''.join(num))*int(''.join(uin_temp)))==int(uin):
            flag = 0
            break
    start+=1
if flag:
    print('Invalid Mutant')
else:
    if n%2: print('Unverified Mutant')
    else: print('Verified Mutant')
