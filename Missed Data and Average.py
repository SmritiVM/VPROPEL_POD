data =[]
element = int(input())
while element!=-1:
    data.append(element)
    element = int(input())
missing_pos,missing_element = int(input()),int(input())
data.insert(missing_pos-1,missing_element)
for num in data:
    print(num,end='\t')
print()
for i in range(0,len(data)-2):
    avg = sum(data[i:i+3])/3
    print(f'{avg:.2f}',end='\t')
