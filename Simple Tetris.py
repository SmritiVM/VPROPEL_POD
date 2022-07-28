n = int(input()) 
stack = []
for i in range(n):
    q = input()
    if q!='2':
        stack.append(q.split()[-1])
        if len(stack)>3:
            if stack[-1]==stack[-2]==stack[-3]==stack[-4]:
                stack = stack[:-4]
    else:
        print(len(stack)) 