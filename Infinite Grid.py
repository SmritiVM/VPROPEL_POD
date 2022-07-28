import math
n = int(input())
point = (1,1)
factors = []
for i in range(1,int(math.sqrt(n)+1)):
    if n%i==0:
        factors.append([i,n//i])
def steps_to(pair):
    steps = pair[0]+pair[1]-2
    return steps
steps_req = n
for pair in factors:
    if steps_to(pair)<steps_req:
        steps_req = steps_to(pair)
print(steps_req)
