'''Word Derivation
A word is made up of symbols from a,b,c...z,0,1,2,3...9. A new word w' generated from a word w by replacing the symbols of w, as prescribed by a rule, expressed as a pair (t,t'), where t and t' are words. Number of symbols in t and t' are same. The rule (t, t') works as follows : If t occurs in w, that is replaced by the word t'. If t occurs at more than one place, the t which occurs in the left most position in w is replaced. For eg, if w=abb, t=ab t'=ba:

'ab' in w is replaced by 'ba'. Thus, a new word bab is derived from the word 'abb' by the application of the rule (ab,ba) once. If we apply the same rule to bab, we get a new word bba.

Thus, we have : abb--->bab--->bba Here, we say that bba is derived from abb in three steps. We can apply the rule any number of times.

Given a word w, a word w' and a rule, write a program to compute whether w' can be derived from w. If w' can be derived from w, your program should output 1, otherwise your program should output 0.

Illustration

Input

aabb

baab

ab

ba

Output

1

Input Format

First line contains the word, w

Next line contains the word, w’

Next line contains contains the word, t

Next line contains contains the word, t’

Output Format

Print 1 if w’ is derivable from w and 0 otherwise'''

w,w_=input(),input()
t,t_ =input(),input()
def apply_rule(w,t,t_):
    w=list(w)
    t=list(t)
    t_=list(t_)
    flag = False
    for i in range(len(w)):
        for j in range(i+1,len(w)):
            if w[i:j+1]==t:
                w[i:j+1]=t_
                flag=True
                break
        if flag:break
    return "".join(w),flag
flag=True
while flag!=False:
    w,flag=apply_rule(w,t,t_)
    if w==w_:
        print('Yes')
        exit(0)
print('No')

##Utttam's
w,wd,t,td,l = input(), input(), input(), input(),""
while l != w:
    l,w = w, w.replace(t,td,1)
    if w == wd: print("Yes"); exit()
else: print("No")
