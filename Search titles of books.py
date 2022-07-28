t = int(input())
n = int(input())
titles = []
for i in range(n):
    titles.append(input())

tot = 0
for i in titles:
    #print(i)
    flag = True

    for j in i:
        if j!= ' ':
            if j.lower() in t or j.upper() in t:
                #print(j,"hey")
                if list(i).count(j.lower())+list(i).count(j.upper())>=list(t).count(j.lower())+list(t).count(j.upper()):
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    if flag:
        print(i)
        tot+=1
if tot==0:
    print("No such book")
