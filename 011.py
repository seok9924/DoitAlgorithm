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
# 백준 1874

# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")


n= int(input())

alist=[]
for i in range(n):
    a=int(input())
    alist.append(a)
stack=[]
num=1
result=True
answer=''
for i in range(n) :
    st=alist[i]
    if st>=num :
        while st>=num :
            stack.append((num))
            num+=1
            answer+='+\n'
        stack.pop()
        answer+='-\n'
    else :
        n=stack.pop()
        if n>st :
            print("NO")
            result=False
            break
        else :
            answer+='-\n'

if result :
    print(answer)