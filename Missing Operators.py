'''Missing Operators
An arithmetic expression was transmitted from one research centre to another. During the transmission, the operators were missed and only the operands were recieved at the other end. It is known that the arithmetic expression consisted of only two operators ‘+’ and ‘-’ and the operands were two 2 digits and one 1 digit number. The evaluated value of the expression is also known. The task is to find the exact expression.

For example, if the value recieved is 87989 and the evaluated value is 7 then the expression is 87+9-89 and if the value recieved is 87989 and the value is 176 then the expression is 8+79+89.

Input Format

First line contains the value at the recieving end, n

Next line is the evaluated value, v

Output Format

Print the expression

Boundary Conditions

Digits in the operands are 1 to 9'''

from itertools import product
n = input()
v = int(input())
n1,n2,n3=n[0],n[1:3],n[3:]
l=[n1,n2,n3]
op=['+','-']
products=list(product(op,repeat=2))
def findexp(products,l,v):
    for p in products:
        test_num = int(l[0])
        exp=l[0]
        for i in range(2):
            exp+=p[i]+l[i+1]
            if p[i]=='+':
                test_num+=int(l[i+1])
            else:
                test_num-=int(l[i+1])
        if test_num==v:
            print(exp)
            exit(0)
findexp(products,l,v)
n1,n2,n3=n[0:2],n[2],n[3:]
l=[n1,n2,n3]
findexp(products,l,v)
