n = int(input()) #no of operations
participants_queue = []
t_shirts_queue = []
for i in range(n):
    choice = int(input())
    if choice==1:
        if i==0:
            p=int(input())
            participants = input().split()
            participants_queue.extend(participants)
        else:
            participants = input().split()
            participants_queue.extend(participants[1:])
        
    elif choice==2:
        m = list(map(int,input().split()))
        t_shirts_queue.extend(m)
        
    else:
        k = int(input())
        for x,y in zip(participants_queue,t_shirts_queue[::-1]):
            if k>0:
                print(x,y)
            k-=1
        participants_queue = participants_queue[k:]
        
