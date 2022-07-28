
n1 = list(map(int,input().split(',')))
n2 = list(map(int,input().split(',')))
k = int(input())

def k_to_decimal(num_list,k):
    dec_num = multiplier = 0
    for i in num_list:
        dec_num+=i*k**(multiplier)
        multiplier+=1
    return dec_num
def convert_to_k(num,k):
    k_num = []
    while num>0:
        k_num.append(num%k)
        num//=k
    return k_num
k1 = k_to_decimal(n1,k)
k2 = k_to_decimal(n2,k)
k_num = convert_to_k(k1+k2,k)
print(*k_num,sep=',')
