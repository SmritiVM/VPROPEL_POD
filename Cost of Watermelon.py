x=int(input())
p1 = int(input())
p2 = int(input())
c = int(input())
non_water = x*(100-p1)//100
new_x = (non_water*100)//(100-p2)
print(c*new_x)
