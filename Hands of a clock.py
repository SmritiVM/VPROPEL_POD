clock = {}
letter = input()
for i in range(1,13):
    clock[i]=letter
    letter = chr(ord(letter)+2)
hour, minute = int(input()),int(input())
if hour>12:
    hour = hour-12
if hour==0:
    hour=12
for hr in clock:
    if hr==hour:
        if minute!=0:
            if hour ==12:
                next_ = clock[1]
            else:
                next_=clock[hr+1]
            print("Between",clock[hr],"and",next_)
        else:
            print("On",clock[hr])
   
if minute==0:
    print("On",clock[12])
elif minute%5==0:
    print("On",clock[minute//5])
else:
    pos_min = minute//5
    if pos_min==0:
        curr_=12
    else:
        curr_=pos_min
    print("Between",clock[curr_],"and",clock[pos_min+1])
