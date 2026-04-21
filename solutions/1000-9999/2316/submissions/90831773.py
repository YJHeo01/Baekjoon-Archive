from collections import deque

import sys

input = sys.stdin.readline

n,p = map(int,input().split())

graph = [[] for _ in range(n+1)]

max_flow = [[0]*(n+1) for _ in range(n+1)]
cur_flow = [[0]*(n+1) for _ in range(n+1)]

for _ in range(p):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    max_flow[a][b] = 1
    max_flow[b][a] = 1

visited = [False] * (n+1)

answer = 0

while True:
    visited[1], visited[2] = False, False
    prev = [-1] * (n+1)
    queue = deque([1])
    while queue and prev[2] == -1:
        x = queue.popleft()
        for nx in graph[x]:
            if max_flow[x][nx] > cur_flow[x][nx] and prev[nx] == -1:
                if visited[nx]: continue
                queue.append(nx)
                prev[nx] = x
                if nx == 2: break
    if prev[2] == -1: break
    flow = 1
    x = 2
    while True:
        if x == 1: break
        cur_flow[prev[x]][x] += flow
        visited[prev[x]] = True
        cur_flow[x][prev[x]] -= flow
        if cur_flow[x][prev[x]] == 0:
            visited[x] = False
        x = prev[x]
    answer += flow
    
print(answer)