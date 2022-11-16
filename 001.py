import math
import sys
from os import path
import itertools

# 백준 11720

if (path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")

n= int(input())
alls=input()
sum=0
for i in alls:
    sum+=int(i)
print(sum)