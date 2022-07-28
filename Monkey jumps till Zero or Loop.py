n = int(input())
array = list(map(int,input().split()))
array.insert(0,0)
pointer=pointer_initial = array[1]
i = 1
print(pointer,end=' ')
while True:
    d = i =abs(array[i]-array[i+1])
    if d==0:
        print()
        print('Happy')
        break

    pointer = array[d]
    print(pointer,end=' ')
    if pointer==pointer_initial:
        print()
        print('Angry')
        break
