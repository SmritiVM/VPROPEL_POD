n = int(input())
elements = {}
for i in range(n):
    ele,symbol = input().split()
    elements[ele]=symbol
choice = int(input())
if choice==1:
    symbol_search = input()
    for ele in elements:
        if elements[ele]==symbol_search:
            print(ele)
            exit(0)
else:
    ele_search = input()
    if ele_search in elements:
        print(elements[ele_search])
        exit(0)
    
print('Not found')
