import math
import sys
from os import path
import itertools
import collections
import heapq
import functools
import re
import bisect
from collections import deque
# 백준 17298

# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")

n=int(input())
alist=list(map(int,input().split()))
stack=[]
answer=[0]*n
for i in range(n) :
    while stack and alist[stack[-1]] <alist[i] :
        answer[stack.pop()]=alist[i]
    stack.append(i)

while stack:
    answer[stack.pop()]=-1

for i in answer :
    print(i,end=' ')