from collections import deque

import sys

input = sys.stdin.readline

INF = 1001

n,m,k = map(int,input().split())

graph = [[[] for _ in range(4)] for _ in range(INF)]

max_flow = [[[[0]*4 for _ in range(INF)] for _ in range(4)] for _ in range(INF)]
cur_flow = [[[[0]*4 for _ in range(INF)] for _ in range(4)] for _ in range(INF)]

max_flow[0][0][0][1] = n + k
max_flow[0][2][0][3] = n + k

graph[0][0].append((0,1))
graph[0][1].append((0,0))
graph[0][2].append((0,3))
graph[0][3].append((0,2))

for i in range(1,m+1):
    max_flow[i][2][i][3] = 1
    max_flow[i][3][0][2] = 1
    graph[i][2].append((i,3))
    graph[i][3].append((i,2))
    graph[0][2].append((i,3))
    graph[i][3].append((0,2))

for i in range(1,n+1):
    graph[0][1].append((i,0))
    graph[i][0].append((0,1))
    max_flow[0][1][i][0] = 2
    max_flow[i][0][i][1] = 2
    graph[i][0].append((i,1))
    graph[i][1].append((i,0))
    tmp = list(map(int,input().split()))
    if tmp[0] == 0: continue
    for j in tmp[1:]:
        max_flow[i][1][j][2] = 1
        graph[i][1].append((j,2))
        graph[j][2].append((i,1))



while True:
    prev = [[(-1,-1)] * 4 for _ in range(INF)]
    queue = deque([(0,0)])
    while queue and prev[0][3] == (-1,-1):
        x,y = queue.popleft()
        for nx,ny in graph[x][y]:
            if max_flow[x][y][nx][ny] > cur_flow[x][y][nx][ny] and prev[nx][ny] == (-1,-1):
                queue.append((nx,ny))
                prev[nx][ny] = (x,y)
                if nx == 0 and ny == 3: break
    if prev[0][3] == (-1,-1): break
    flow = 1
    x,y = 0,3
    while True:
        if x == 0 and y == 0: break
        pre_x, pre_y = prev[x][y]
        cur_flow[pre_x][pre_y][x][y] += flow
        cur_flow[x][y][pre_x][pre_y] -= flow
        x,y = pre_x, pre_y

    
print(cur_flow[0][2][0][3])