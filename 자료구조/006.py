import math
import sys
from os import path
import itertools

# 백준 2018

# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")
input =sys.stdin.readline
n= int(input())
count = 1
start_index= 1
end_index= 1
sum=1
while end_index != n:
    if sum==n:
        count+=1
        end_index+=1
        sum+=end_index
    elif sum>n:
        sum-= start_index
        start_index+=1
    else:
        end_index+=1
        sum+=end_index

print(count)