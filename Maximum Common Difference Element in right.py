n = int(input())
l = list(map(int,input().split()))
diff = {}
diff_values = []
for i in range(n-1):
    for j in range(i+1,n):
        d = abs(l[i]-l[j])
        if l[i] not in diff:
            diff[l[i]]=[d]
        else:
            diff[l[i]].append(d)
    diff_values.extend(set(diff[l[i]]))
max_count = 0
common_diff = 0
for val in diff_values:
    if diff_values.count(val)>max_count:
        max_count = diff_values.count(val)
        common_diff = val
print(common_diff)
result_list = []
for num in diff:
    if common_diff in diff[num]:
        result_list.append(num)
print(*sorted(result_list))
