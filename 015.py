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
# 백준 2750

# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")
input =sys.stdin.readline

n= int(input())

a=[]
for i in range(n) :
    a.append(int(input()))
for i in range(n-1) :
    for j in range(n-i-1) :
        if a[j]>a[j+1] :
            a[j+1],a[j] = a[j],a[j+1]
for i in range(n):
    print(a[i])

