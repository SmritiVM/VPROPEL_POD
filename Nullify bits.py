n = int(input())
b = bin(n)[2:]
new_b = ''
odd_bit_value = even_bit_value = 0
for i in range(len(b)):
    if i%2 and b[i]=='1':
        odd_bit_value+=1
    elif not i%2 and b[i]=='1':
        even_bit_value+=1
if odd_bit_value<even_bit_value:
    for i in range(len(b)):
        if i%2 and b[i]=='1':
            new_b+='0'
        else:
            new_b+=b[i]
else:
    for i in range(len(b)):
        if not i%2 and b[i]=='1':
            new_b+='0'
        else:
            new_b+=b[i]
def decimal(bin_num):
    dec_num = 0
    for i in range(len(bin_num)):
        dec_num+=int(bin_num[i])*(2**i)
    return dec_num

print(decimal(new_b[::-1]))
