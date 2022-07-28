#Letter Partner Game easier
s = input()
stack = []

def is_pre_partner(char):
    if ord(char)-ord('a')<13: return True
    return False

def find_pre_partner(char):
    return chr(ord(char)-13)

for ch in s:
    if is_pre_partner(ch):
        stack.append(ch)

    else:
        pre_par_ch = find_pre_partner(ch)

        if stack==[] or not stack.pop()==pre_par_ch:
            print('Lost')
            break
else:
    if stack ==[]:
        print('Won')
    else:
        print('Lost')
