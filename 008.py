import math
import sys
from os import path
import itertools

# 백준 1253

# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")
input =sys.stdin.readline

N= int(input())
A= list(map(int,input().split()))
answer= 0
A.sort()

for k in range(N) :
    find =A[k]
    i=0
    j=N-1
    while i<j:
        if A[i] +A[j] ==find :
            if i!=k and j!=k :
                answer+=1
                break
            elif i==k:
                i+=1
            elif j==k:
                j-=1
        elif A[i]+A[j] <find :
            i+=1
        else :
            j-=1
print(answer)