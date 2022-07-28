from queue import PriorityQueue
n = int(input())#no.of pipes
pipes = PriorityQueue()
for i in range(n):
    pipes.put(int(input()))


length = 0
while pipes.qsize()>1:
    a = pipes.get()
    b = pipes.get()
    length+=a+b
    pipes.put(a+b)
    
    
if n>1:
    print(length)
else:
    print(pipes.get())
