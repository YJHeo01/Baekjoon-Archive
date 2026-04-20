from collections import deque

import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [[[] for _ in range(2)] for _ in range(n+m+2)]

max_flow = [[[[0]*2 for _ in range(n+m+2)] for _ in range(2)] for _ in range(n+m+2)]
cur_flow = [[[[0]*2 for _ in range(n+m+2)] for _ in range(2)] for _ in range(n+m+2)]

graph[0][0].append((0,1))
graph[0][1].append((0,0))

max_flow[0][0][0][1] = n+k

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    graph[0][1].append((i,0))
    graph[i][0].append((0,1)) #원점 - 정점
    max_flow[0][1][i][0] = tmp[0]
    graph[i][0].append((i,1))
    graph[i][1].append((i,0))
    max_flow[i][0][i][1] = k + 1 #정점 분할(직원원)
    for j in tmp[1:]:
        graph[i][1].append((n+j,0))
        graph[n+j][0].append((i,1))
        max_flow[i][1][n+j][0] = 1 #직원 - 일 연결

for j in range(1,m+1):
    graph[n+j][0].append((n+j,1))
    graph[n+j][1].append((n+j,0))
    max_flow[n+j][0][n+j][1] = 1 #정점 분할(일)
    graph[n+j][1].append((n+m+1,0))
    graph[n+m+1][0].append((n+j,1))
    max_flow[n+j][1][n+m+1][0] = 1 #일 - 종착지 연결
    
graph[n+m+1][0].append((n+m+1,1))
graph[n+m+1][1].append((n+m+1,0))
max_flow[n+m+1][0][n+m+1][1] = m #종착지 정점 분할

answer = 0

while True:
    prev = [[(-1,-1)]*2 for _ in range(n+m+2)]
    queue = deque([(0,0)])
    while queue and prev[n+m+1][1] == (-1,-1):
        x,y = queue.popleft()
        for nx,ny in graph[x][y]:
            if max_flow[x][y][nx][ny] > cur_flow[x][y][nx][ny] and prev[nx][ny] == (-1,-1):
                queue.append((nx,ny))
                prev[nx][ny] = (x,y)
    if prev[n+m+1][1] == (-1,-1): break
    flow = n+m+k
    cur_x, cur_y = n+m+1,1
    while True:
        if cur_x == 0 and cur_y == 0: break
        prev_x, prev_y = prev[cur_x][cur_y]
        flow = min(flow,max_flow[prev_x][prev_y][cur_x][cur_y]-cur_flow[prev_x][prev_y][cur_x][cur_y])
        cur_x,cur_y = prev_x,prev_y
    cur_x, cur_y = n+m+1,1
    answer += flow
    while True:
        if cur_x == 0 and cur_y == 0: break
        prev_x, prev_y = prev[cur_x][cur_y]
        cur_flow[prev_x][prev_y][cur_x][cur_y] += flow
        cur_flow[cur_x][cur_y][prev_x][prev_y] -= flow
        cur_x,cur_y = prev_x,prev_y
        
print(answer)