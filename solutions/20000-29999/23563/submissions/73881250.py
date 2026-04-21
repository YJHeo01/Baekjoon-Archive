from collections import deque
import sys

input = sys.stdin.readline

h,w = map(int,input().split())

board = []

start,end = (-1,-1),(-1,-1)

for i in range(h):
    tmp = list(input())
    board.append(tmp)
    for j in range(w):
        if tmp[j] == 'S':
            start = (i,j)
        elif tmp[j] == 'E':
            end = (i,j)
        else:
            continue

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check_warp_zone(graph,visited,warp_zone,start):
    queue = deque([start])
    visited[0][start[0]][start[1]],visited[1][start[0]][start[1]] = True,True
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[nx][ny] == '#' and visited[i//2][nx][ny] == False:
                visited[i//2][nx][ny] = True
                if i < 2:
                    for zone_y in [vy-1,vy+1]:
                        if zone_y < 0 or zone_y >= w:
                            continue
                        for zone_x in [vx,nx]:
                            warp_zone[0][zone_x][zone_y] = True
                else:
                    for zone_x in [vx+1,vx-1]:
                        if zone_x < 0 or zone_x >= h:
                            continue                        
                        for zone_y in [vy,ny]:
                            warp_zone[1][zone_x][zone_y] = True
                queue.append((nx,ny))


visited = [[[False]*w for _ in range(h)]for _ in range(2)]
warp_zone = [[[False]*w for _ in range(h)]for _ in range(2)]

for i in range(h):
    for j in range(w):
        if board[i][j] == '#' and visited[0][i][j] == False:
            check_warp_zone(board,visited,warp_zone,(i,j))

def solution(graph,time,warp_zone,start):
    queue = deque([start])
    time[start[0]][start[1]] = 0
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '#':
                continue
            if warp_zone[i//2][vx][vy] == True and warp_zone[i//2][nx][ny] == True:
                dt = 0
            else:
                dt = 1
            if time[nx][ny] > time[vx][vy] + dt:
                time[nx][ny] = time[vx][vy] + dt
                queue.append((nx,ny))

INF = int(1e9)
time = [[INF]*w for _ in range(h)]

solution(board,time,warp_zone,start)

print(time[end[0]][end[1]])