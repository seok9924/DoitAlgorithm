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
from queue import PriorityQueue
import heapq
# 백준 11286
# 우선순위 큐 사용법 익히기  <==== 중요


if (path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")
# input =sys.stdin.readline


n=int(input())

dq =[]
# heapq로 해보기 sys.stdin 안했더니 시간초과뜸
for i in range(n):
    x=int(input())

    if x==0:
        if dq :
            print(heapq.heappop(dq)[1])
        else:
            print(0)

    else:
        heapq.heappush(dq,(abs(x),x))

#
# # 우선순위큐 역시 같음
# pq=PriorityQueue()
# for i in range(n):
#     x=int(input())
#
#     if x==0:
#         if pq.empty() :
#             print(0)
#         else:
#             temp=pq.get()
#             print(str((temp[1])))
#
#     else:
#         pq.put((abs(x),x))  #우선순위 큐
#
#



