import math
import sys
#from os import path
import itertools

#백준 11659
                         #------------- > path 사용시 시간 초과뜸 path 사용을 줄여보자
                        
# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")
input =sys.stdin.readline

a,b=map(int,input().split())
arr=list(map(int,input().split()))

prefix_sum=[0]
temp=0
# 할때마다 계산하는 절차를 밟기보다는 값을 저장해두고 꺼내쓰는 절차

for i in arr :
    temp=temp+i
    prefix_sum.append(temp)


for i in range (b) :
    c,d=map(int,input().split())
    print(prefix_sum[d]-prefix_sum[c-1])