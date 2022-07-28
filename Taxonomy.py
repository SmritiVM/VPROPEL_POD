n = int(input()) #No. of taxonomies
tax_col={}#collection of all taxonomies

for i in range(n):
    l0 = input()#0 level
    l1 = list(input().split())#elements of level 1
    l1_dict = {}
    for ele in l1:
        l1_dict[ele]='None'
    for j in range(len(l1)):
        l2 = list(input().split())#elements of level 2
        if 'None' not in l2:
            l1_dict[l2[0]]=l2[1:]
    tax_col[l0]=l1_dict

p = input()#element to be checked at level 0
l1 = input()#element to be checked at level 1, l1
l2 = input()#element to be checked at level 2, l2

flag = True
if p in tax_col:
    for i in tax_col[p]:
        if i==l1 and l2 in tax_col[p][l1]:
            flag = False
            print('Taxonomy present')
            break
        
if flag:
    print('Taxonomy not present')
