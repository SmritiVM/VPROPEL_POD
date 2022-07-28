'''New clock dial
All of us are familiar with the usual clock with a circular dial of of having sixty dots.  Of course,  there are numbers 1, 2,3,...,10,11,12, after every 5 dots. For example,  Number 2 is placed  exactly at the fifth dot after the number 1.  Consider a new dial with sixty dots, but numbered with  three numbers 1,2,3.  Number 1 in the new dial is in the position where 12 occurs in the old dial, number 2  is placed after 19 dots in usual clock-wise direction, and number 3 is placed after 19 dots after the number 2., in the usual clock-wise direction   There are 19 dots berween each number in the new dial.  As usual, the new dial has two arms: Hour arm and the minute arm.  If the hour arm is pointing to 3 and the minutes arm is pointing to 1,  usual time  (in the usual dial) is 8 hrs 0 minutes.  Given the time in the new dial with the positions of hour arm and the minute arm,  write a code to compute the time in hours & minutes in our usual  standard time. Assume that all the time considered here are in A.M category.

Position of the hour arm is indicated by a pair of numbers (x,y) called Position Pair,  where x is either 1 or 2,or 3 in the new dial., y-represents the number of points after x. For eg., if the position of hour arm is (2,30), this means that the hour arm is in the thirtieth dot after the number 2, in the usual clockwise direction.  The position (2,0) means that the hour arm is positioned at number 2 in the new dial.  Similarly, the position of the minute arm is represented as a pair of integers.

 

Input format :

Enter first component of the position pair of the hour arm

Enter second component of the position pair of the hour arm

Enter first component of the position pair of the minute arm

Enter second  component of the position pair of the minute arm

 

Output format 

Enter the hour in the usual time (2 digit format)

Enter the minutes in the usual time (2 digit format)

Illustration:

Input

3

0

1

0

Output

08

00'''

hx,hy=int(input()),int(input())
mx,my=int(input()),int(input())
d = {1:0,2:20,3:40}
hpointer = d[hx]+hy
if hpointer==0: hour='12'
else: hour=str(hpointer//5)
if len(hour)<2: print('0'+hour)
else: print(hour)
minute = str(d[mx]+my)
if len(minute)<2: print('0'+minute)
else: print(minute)

###
hx,hy,mx,my = int(input()),int(input()),int(input()),int(input())
nh = (hx - 1)*4 + hy//5
nm = (mx - 1)*20 + my
if nh == 0: nh = 12
print(f"{nh:02d}\n{nm:02d}") 
