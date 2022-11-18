import math
import sys
from os import path
import itertools

# 백준 10986
# ------------- > path 사용시 시간 초과뜸 path 사용을 줄여보자
# https://www.youtube.com/watch?v=Ud-qe0t5KA8&ab_channel=%ED%95%98%EB%A3%A8%EC%BD%94%EB%94%A9
# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")
input =sys.stdin.readline

n,m = map(int,input().split())
arr= list(map(int,input().split()))
prefix_arr=[0]*n
C=[0]*m
prefix_arr[0]=arr[0]
answer=0
for i in range(1,n):
    prefix_arr[i]=prefix_arr[i-1]+arr[i]


for i in range(n):
    remainder=prefix_arr[i]%m
    if remainder==0:
        answer+=1
    C[remainder]+=1

for i in range(m) :
    if C[i]>1 :
        answer+=(C[i]*(C[i]-1)//2)
print(answer)