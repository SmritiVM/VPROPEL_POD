n = int(input())
heights = list(map(int,input().split()))
steps = [heights[0]]
longest_step = steps
for i in range(1,n):
    if heights[i]>steps[-1]:
        steps.append(heights[i])
    else:
        steps = [heights[i]]
    if len(steps)>len(longest_step):
        longest_step=steps

for i in range(n):
    if heights[i]==longest_step[0]:
        low_ind=i
        break
print(low_ind+1,low_ind+len(longest_step))