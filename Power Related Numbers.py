import math
l = int(input())
u = int(input())
p = int(input())
min_pow_num = [u,u,u]
max_pow_num = [0,0,0]

for n in range(l,u):
    for p_ in range(2,p+1):
        power_num = int(math.pow(n,p_))
        sum_of_dig = 0
        for i in str(power_num):
            sum_of_dig+=int(i)
        if sum_of_dig==n:   
            if n<min_pow_num[0] and p_<min_pow_num[1]:
                min_pow_num=[n,p_,power_num]
            if n>max_pow_num[0]:
                max_pow_num=[n,p_,power_num]
print(*min_pow_num)
print(*max_pow_num)
