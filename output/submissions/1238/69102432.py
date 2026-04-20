from collections import deque

import sys

input = sys.stdin.readline

INF = int(1e9)

n,m,x = map(int,input().split())
jump = deque([])
time = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    start, end, t = map(int,input().split())
    time[start][end] = t
    jump.append((start,end))

while(jump):
    start,end = jump.popleft()
    for i in range(1,n+1):
        if time[start][i] > time[start][end] + time[end][i]:
            time[start][i] = time[start][end] + time[end][i]
            jump.append((start,i))
answer = 0
for i in range(1,n+1):
    answer = max(answer,time[i][x]+time[x][i])

print(answer)