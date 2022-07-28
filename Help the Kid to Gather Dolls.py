n = int(input())
dolls = [input().lower() for i in range(n)]
doll_box={}
def calc_box(doll):
    start = doll[0]
    end = doll[-1]
    if start>end: start,end=end,start
    count = 0
    for i in doll:
        if i>=start and i<=end:
            continue
        else:
            count+=1
    return count+1

for doll in dolls:
    doll_box[doll]=calc_box(doll)
    
pos = 0
a = 0
count = 0
while a<n:
    doll = dolls[a]
    req_pos = doll_box[doll]
    if req_pos>pos:
        diff = req_pos-pos
        print('f',diff,sep='\t')
    elif pos>req_pos:
        diff = pos-req_pos
        print('b',diff,sep='\t')
    else:
        diff = 0
        print('n',diff,sep='\t')
    pos = req_pos
    a+=1
    count+=diff
print(count)
    