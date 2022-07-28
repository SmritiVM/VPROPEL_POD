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


##LAR's code
n=int(input())
k=int(input())
d=2
z=[]
a=(n-k*(k-1))/k
if a%1!=0:
    print("Cannot be built")
else:
    a=int(a)
    for i in range(0,k,1):
        z.append(a+i*d)
        #print(a+i*d,sep="\t")
    for i in z:
        print(i,end="\t")
