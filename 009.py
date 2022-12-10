import math
import sys
from os import path
import itertools
import collections
import heapq
import functools
import re
import bisect

# 백준 12891

if (path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")



# input =sys.stdin.readline




n,s=map(int,input().split())
dna=input()
A,C,G,T=list(map(int,input().split()))   #A,C,G,T
ACGTdic={'A':0,"C":0,"G":0,'T':0}

answer=0

for i in range(s):
    ACGTdic[dna[i]]+=1

if ACGTdic['A'] >= A and ACGTdic['C'] >= C and ACGTdic['G'] >= G and ACGTdic['T'] >= T:
    answer += 1

for i in range(s,n) :

    ACGTdic[dna[i-s]] -= 1
    ACGTdic[dna[i]] += 1
    if ACGTdic['A'] >= A and ACGTdic['C'] >= C and ACGTdic['G'] >= G and ACGTdic['T'] >= T:
        answer += 1
print(answer)





