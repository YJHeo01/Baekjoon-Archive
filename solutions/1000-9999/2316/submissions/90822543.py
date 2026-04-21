from collections import deque

import sys

input = sys.stdin.readline

n,p = map(int,input().split())

graph = [[] for _ in range(n+1)]

max_flow = [0] * (n+1)
cur_flow = [0] * (n+1)
for _ in range(p):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    max_flow[b] = 1

answer = 0

while True:
    prev = [-1] * (n+1)
    queue = deque([1])
    while queue and prev[2] == -1:
        x = queue.popleft()
        for nx in graph[x]:
            if max_flow[nx] > cur_flow[nx] and prev[nx] == -1:
                queue.append(nx)
                prev[nx] = x
                if nx == 2: break
    if prev[2] == -1: break
    flow = 1
    x = 2
    while True:
        if x == 1: break
        cur_flow[prev[x]] += flow
        x = prev[x]
    answer += flow
    
print(answer)