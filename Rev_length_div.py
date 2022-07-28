n = int(input())
a = 1
b=''
def div(num):
    global a,b
    if num>0:
        if num%a==0:
            num//=10
            a+=1
            b='Yes'
            div(num)
            
        
        else:
            b='No'
    
    
        
div(n)
print(b)


        
        
