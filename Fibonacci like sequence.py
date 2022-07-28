'''Fibanocci Like Sequence
Vijay observed some properties by examining the fibanocci like sequences. One of his observation is related to the fifth term and the sum of first six terms in the sequence. He told his friend that given the sixth term of the sequence and the sum of first six terms of a sequence, it is possible to generate the six terms of the sequence in reverse. For example, if the 6th term is 5 and sum is 12 then the first six terms of the sequence in reverse are 5, 3, 2, 1, 1, 0.

Given the sixth term and sum of first six terms of a fibanocci like sequence, generate six terms of the sequence in reverse.

 

Input Format

First line contains the sixth term of the sequence

Next line contains the sum of first six terms of the sequence

Output Format

Print the six terms of the sequence in reverse '''
seq = [int(input()),0,0,0,0,0]
sum_of_seq = int(input())
for i in range(seq[0]-1,-1,-1):
    seq[1]=i
    for j in range(2,6):
        seq[j]=seq[j-2]-seq[j-1]
    if sum(seq)==sum_of_seq:
        print(*seq)
        exit()
