x = int(input())
w1 = int(input())
w2 = int(input())
n = int(input())
if w1>w2:
    w1,w2=w2,w1
new_weights = list(map(int,input().split()))
vals = []
for weight in new_weights:
    weight-=x
    if weight%w1 == 0 or weight%w2 == 0:
        vals.append(1)
        
    else:
        a = weight//w2
        w_ = weight - w2*a
        b = w_//w1
        if weight==w1*b+w2*a:
            vals.append(1)
        else:
            vals.append(0)
print(*vals)
