m = int(input())
schedules = [list(map(int,input().split())) for i in range(m)]
n = int(input())
solve_sched = [list(map(int,input().split())) for i in range(n)]
completed = 0

for sched in schedules:
    date = sched[0]
    no_of_problems = sched[1]
    total_probs_solved= 0
    for stud_sched in solve_sched:
        if stud_sched[0]<=date:
            total_probs_solved+=stud_sched[1]
        if stud_sched[0]>=date:
            if total_probs_solved>no_of_problems:
                completed+=1
                break
        
    
mid = m/2 if m%2==0 else (m+1)/2
if completed<mid:
    print("Denied")
else:
    print("Allowed")
