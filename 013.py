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
# 백준 2164

if (path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")
dq = deque()
n= int(input())
for i in range(1,n+1):
    dq.append(i)

while len(dq)>1:
    dq.popleft()
    dq.append(dq.popleft())
print(dq[0])