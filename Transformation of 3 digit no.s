def unique2(num):
    if len(set(str(num)))>=2:
        return True
    return False

def diff(num):
    m1 = int(''.join(sorted(list(str(num)))))
    m2 = int(''.join(sorted(list(str(num)),reverse = True)))
    ans = str(m2-m1)
    if len(ans)<3:
        ans+='0'
    return int(ans)

l = []
def transform(num):
    global l
    if num==495:
        return len(l)-1
    else:
        l.append(diff(num))
        return transform(diff(num))

n = int(input())
if unique2(n):
    print(transform(n))
else:
    print('No')
