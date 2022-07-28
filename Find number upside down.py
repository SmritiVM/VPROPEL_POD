diff = int(input())
n = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
req = []
for i in n:
    for j in n:
        num = int(i)*10+int(j)
        flip_num =int(n[j])*10+int(n[i])
        d = abs(flip_num-num)
        #print(num,flip_num)
        if d==diff:
            if num>flip_num:
                req = [n[j]+n[i],i+j]
            else:
                req = [i+j,n[j]+n[i]]
print(*req)
