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
# 백준 11003

# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")



input =sys.stdin.readline

# min() 도 정렬알고리즘으로 생각해야함
n,l =map(int,input().split())
a = list(map(int,input().split()))
dq=deque()


for i in range(n) :
    while dq and dq[-1][0] >a[i] :
        dq.pop()

    dq.append((a[i],i))


    if dq[0][1] <= i-l :
        dq.popleft()
    print(dq[0][0],end=' ')

