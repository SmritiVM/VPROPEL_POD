w1,w2 = list(input()),list(input())
num = []
if len(w2)>len(w1):
    w1,w2=w2,w1
max_length=len(w1)
carry = 0
while w2:
    sum_ = str(ord(w2.pop())+ord(w1.pop())+carry)
    carry = int(sum_[:-1])
    num.insert(0,sum_[-1])
    if not w2 and not w1:
        num.insert(0,str(carry))

if w1:
    n = 0
    for i in range(len(w1)):
        n+=ord(w1[i])*10**i
    n+=carry
    num.insert(0,str(n))
        
        
def convert_alpha(number):
    if number>=26:
        char = 97+number-25-1
    else:
        char = 97+number
    return chr(char)

num = list("".join(num))
i=0
res = []
while True:
    while i<max_length:
        ele = num.pop()
        res.append(convert_alpha(int(ele)))
        i+=1
    else:
        num = "".join(num)
        res.append(convert_alpha(int(num)))
        break
print("".join(res)[::-1])
