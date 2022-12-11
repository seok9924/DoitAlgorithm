import math
import sys
from os import path
import itertools

# 백준 11660
# ------------- > path 사용시 시간 초과뜸 path 사용을 줄여보자

# if (path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")
input =sys.stdin.readline

n,m = map(int,input().split())   #n by n의 행렬 받음  m 개의 질문 받음
arr = [list(map(int,input().split()))for _ in range (n)]


prefix_arr= [[0 for j in range (n+1)]for i in range(n+1)]

for i in range(1,n+1) :
    for j in range(1, n+1) :
        prefix_arr[i][j]= prefix_arr[i][j-1]+prefix_arr[i-1][j]-prefix_arr[i-1][j-1]+arr[i-1][j-1]
        
#

for k in range(m) :
    x1,y1,x2,y2 = map(int,input().split())
    print(prefix_arr[x2][y2]-prefix_arr[x1-1][y2]-prefix_arr[x2][y1-1]+prefix_arr[x1-1][y1-1])
    
# 주의 ! 마지막에 x1-1 y1-1 더해주기

