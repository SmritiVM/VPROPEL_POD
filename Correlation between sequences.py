n_plus1= int(input())
g1 = list(map(float,input().split()))
g2 = list(map(float,input().split()))
error_pos_g1 = int(input())
error_pos_g2 = int(input())
def remove_errors(error_pos,g):
    
    g.pop(error_pos-1)
    for i in g:
        if i-int(i)==0: i=int(i)
        print(i,end=' ')
    print()
remove_errors(error_pos_g1,g1)
remove_errors(error_pos_g2,g2)

if g1==g2:
    print('Equal')
elif all([round(abs(g1[i]-g2[i]))==round(abs(g1[i+1]-g2[i+1])) for i in range(n_plus1-2)]):
    print('Good')
else:
    print('Bad')
