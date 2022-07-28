n, r = int(input()),int(input())
#for rth row..a = r, d = 2*a, s = n/2(2a + (n-1)d), n = r
print((r*(2*r + (r-1)*2*r))//2)
total_sum = 0
for i in range(1,n+1):
    total_sum+=(i*(2*i + (i-1)*2*i))//2
print(total_sum)
print(sum([(i*(2*i + (i-1)*2*i))//2 for i in range(1,n+1)]))
