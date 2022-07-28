a,b,c = int(input()),int(input()),int(input())
nums = [a,b,c]
min_num = min(nums)

nums.remove(min_num)
min_val1 = min_num-(sum(nums))
pdt = 1
for i in nums:
    pdt*=i
min_val2 = min_num-pdt
if (min_val2<min_val1):
    print(min_val2)
else:
    print(min_val1)
