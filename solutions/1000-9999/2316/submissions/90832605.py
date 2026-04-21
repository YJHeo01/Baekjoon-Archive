from collections import deque

import sys

input = sys.stdin.readline

n,p = map(int,input().split())

graph = [[[] for _ in range(2)] for _ in range(n+1)]

max_flow = [[[[0]*2 for _ in range(n+1)] for _ in range(2)] for _ in range(n+1)]
cur_flow = [[[[0]*2 for _ in range(n+1)] for _ in range(2)] for _ in range(n+1)]

for i in range(1,n+1):
    max_flow[i][0][i][1] = 1
    graph[i][0].append((i,1))
    graph[i][1].append((i,0))

for _ in range(p):
    a,b = map(int,input().split())
    graph[a][1].append((b,0))
    graph[b][1].append((a,0))
    graph[a][0].append((b,1))
    graph[b][0].append((a,1))
    max_flow[a][1][b][0] = 1
    max_flow[b][1][a][0] = 1

answer = 0

while True:
    prev = [[(-1,-1)] * 2 for _ in range(n+1)]
    queue = deque([(1,1)])
    while queue and prev[2][0] == (-1,-1):
        x,y = queue.popleft()
        for nx,ny in graph[x][y]:
            if max_flow[x][y][nx][ny] > cur_flow[x][y][nx][ny] and prev[nx][ny] == (-1,-1):
                queue.append((nx,ny))
                prev[nx][ny] = (x,y)
                if nx == 2 and ny == 0: break
    if prev[2][0] == (-1,-1): break
    flow = int(1e9)
    x,y = 2,0
    while True:
        if x == 1 and y == 1: break
        pre_x, pre_y = prev[x][y]
        flow = min(flow,max_flow[pre_x][pre_y][x][y]-cur_flow[pre_x][pre_y][x][y])
        x,y = pre_x, pre_y
    x,y = 2,0
    while True:
        if x == 1 and y == 1: break
        pre_x, pre_y = prev[x][y]
        cur_flow[pre_x][pre_y][x][y] += flow
        cur_flow[x][y][pre_x][pre_y] -= flow
        x,y = pre_x, pre_y
    answer += flow
    
print(answer)