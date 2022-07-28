n=int(input()) #no. of lines
points = []
for i in range(n):
    points.append(list(map(int,input().split())))
   
chp = int(input()) #Check point

line=[] #stores points which can be linked
pointer = [] #pointer instance
for i in points:
    if i[0]==chp:
        pointer=i

line.append(pointer)  

#Function to find the point that can be joined to given point
def linecon(pointer):
    global line,points
    for i in points:
        try:
            if i[0]==pointer[1]:
                line.append(i)
                pointer = i
                return pointer
        except:
            return False
    
    
ogpointer = pointer.copy()        
for i in range(n):
    pointer = linecon(pointer)
    if pointer==ogpointer or pointer==False:
        break
    
if line.count(ogpointer)!=2:
    print(0)
    
else:
    print(len(line)-1)
