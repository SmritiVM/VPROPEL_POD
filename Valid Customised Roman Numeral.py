r = input()
numerals = {'I':1,'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}

def check_valid(r):
    l = list(r)
    if l.count('V')>1 or l.count('L')>1 or l.count('D')>1:
        return False
    for i in range(len(r)-1):
        if numerals[r[i]]<numerals[r[i+1]] and r[i] not in ['V','L','D']:
            l1 = list(r[:i+1])
            if l1.count(r[i])>2:
                return False
    return True

def convert(r):
    hindu_arab = 0
    for i in range(len(r)-1):
        #print(hindu_arab)
        if numerals[r[i]]<numerals[r[i+1]]:
            hindu_arab-=numerals[r[i]]
        elif numerals[r[i]]==numerals[r[i+1]]:
            if i!=len(r)-1:
                if numerals[r[i+1]]<numerals[r[i+2]]:
                    hindu_arab-=numerals[r[i]]
                else:
                    hindu_arab+=numerals[r[i]]
        else:
            hindu_arab+=numerals[r[i]]
    hindu_arab+=numerals[r[-1]]
    return hindu_arab
if check_valid(r):
    print(convert(r))
else:
    print("Invalid")
