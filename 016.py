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
# 백준 1377

if (path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")


# input =sys.stdin.readline

n=int(input())
a=[]
answer=0
for i in range(n) :
    a.append((int(input()),i))
at=sorted(a)

for i in range(n) :
    if answer<at[i][1]-i:
        answer=at[i][1]-i
print(answer+1)
