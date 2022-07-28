import re
s = input()
id = re.findall('([a-zA-Z]+)\[([a-zA-Z]+-\d+)\]',s)

if len(id)>0:
    for i in id:
        print(i[0],i[1])
else:
    print('-1')
