import math
import sys
from os import path
import itertools

#백준 1546

if (path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")
n= int(input())
a_list=list(map(int,input().split()))
max_number=max(a_list)
b_list=list(map(lambda x: x/max_number*100,a_list))
print(sum(b_list)/n)
