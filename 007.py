import math
import sys
from os import path
import itertools

# 백준 1940

# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")
input =sys.stdin.readline
N= int(input())
M= int(input())
A= list(map(int,input().split()))
A.sort()
count=0
i=0
j=N-1
while i<j :
    if A[i] +A[j] <M :
        i+=1
    elif A[i] +A[j] >M:
        j-=1
    else :
        count+=1
        i+=1
        j-=1
print(count)