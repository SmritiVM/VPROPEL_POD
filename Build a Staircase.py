n = int(input())
k = int(input())
mid_num = n//k
if k%2:
    r_num = []
    for i in range(1,k//2+1):
        r_num.append(mid_num-2*i)
    l_num = []
    for i in range(1,k//2+1):
        l_num.append(mid_num+2*i)
    nums = r_num + [mid_num] + l_num
else:
    r_num = []
    for i in range(1,k//2+1):
        r_num.append(mid_num+1-2*i)
    l_num = []
    for i in range(1,k//2+1):
        l_num.append(mid_num-1+2*i)
    nums = r_num + l_num
nums.sort()
if sum(nums)==n:
    print(*nums,sep='\t')
else:
    print('Cannot be built')
