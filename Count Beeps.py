n = input()
m = len(n)
def bin_conv(num):
    num=num[::-1]
    dec_num = 0
    for i in range(len(num)):
        dec_num+=2**i*int(num[i])
    return dec_num
    
def beep(num):
    dec_num = bin_conv(num)
    if dec_num%2==0:
        return True
    return False
    
beep_count=0
for i in range(m-1):
    if beep(n):
        beep_count+=1
    n = n[-1]+n[:-1]
print(beep_count)
