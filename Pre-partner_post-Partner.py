import string
def pre_part(char):
    if char in string.ascii_lowercase[:13]:
        return True
    return False
        
def corr_part(ch1,ch2):
    if ord(ch2)-ord(ch1)==13:
        return True
    return False

w = input().lower()
l = []
for i in w:
    if pre_part(i):
        l.append(i)
        
    else:
        if not l:
            print('Lost')
            break
        
        else:
            ch = l.pop(-1)
            if corr_part(ch,i):
                continue
            else:
                print('Lost')
                break
            
else:
    if not l:
        print('Won')
    else:
        print('Lost')
        
