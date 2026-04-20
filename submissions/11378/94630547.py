from collections import deque

import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [[[] for _ in range(4)] for _ in range(1001)]

graph[0][0].append([0,1,n+k])
graph[0][1].append([0,0,0])

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    graph[0][1].append([i,0,tmp[0]])
    graph[i][0].append([0,1,0]) #원점 - 정점
    #max_flow[0][1][i][0] = tmp[0]
    graph[i][0].append([i,1,k+1])
    graph[i][1].append([i,0,0])
    #max_flow[i][0][i][1] = k + 1 #정점 분할(직원원)
    for j in tmp[1:]:
        graph[i][1].append([j,2,1])
        graph[j][2].append([i,1,0])
    #    max_flow[i][1][j][2] = 1 #직원 - 일 연결

for j in range(1,m+1):
    graph[j][2].append([j,3,1])
    graph[j][3].append([j,2,0])
    #max_flow[j][2][j][3] = 1 #정점 분할(일)
    graph[j][3].append([0,2,1])
    graph[0][2].append([j,3,0])
    #max_flow[j][3][0][2] = 1 #일 - 종착지 연결
    
graph[0][2].append([0,3,m])
graph[0][3].append([0,2,0])
#max_flow[0][2][0][3] = m #종착지 정점 분할

answer = 0

while True:
    prev = [[(-1,-1)]*4 for _ in range(1001)]
    queue = deque([(0,0)])
    while queue and prev[0][3] == (-1,-1):
        x,y = queue.popleft()
        for nx,ny,cap in graph[x][y]:
            if cap and prev[nx][ny] == (-1,-1):
                queue.append((nx,ny))
                prev[nx][ny] = (x,y)
    if prev[0][3] == (-1,-1): break
    flow = n+m+k
    cur_x, cur_y = 0,3
    while True:
        if cur_x == 0 and cur_y == 0: break
        prev_x, prev_y = prev[cur_x][cur_y]
        for tmp_x,tmp_y,cap in graph[prev_x][prev_y]:
            if tmp_x == cur_x and tmp_y == cur_y:
                flow = min(flow,cap)
                break
        cur_x,cur_y = prev_x,prev_y
    cur_x, cur_y = 0,3
    answer += flow
    while True:
        if cur_x == 0 and cur_y == 0: break
        prev_x, prev_y = prev[cur_x][cur_y]
        idx = 0
        for tmp_x,tmp_y,cap in graph[prev_x][prev_y]:
            if tmp_x == cur_x and tmp_y == cur_y:
                graph[prev_x][prev_y][idx][2] -= flow
                break
            idx += 1
        idx = 0
        for tmp_x,tmp_y,cap in graph[cur_x][cur_y]:
            if tmp_x == prev_x and tmp_y == prev_y:
                graph[cur_x][cur_y][idx][2] += flow
                break
            idx += 1
        cur_x,cur_y = prev_x,prev_y
        
print(answer)