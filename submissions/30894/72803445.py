from collections import deque

n,m = map(int,input().split())

house = []

start_x, start_y, end_x, end_y = map(int,input().split())
start_x-=1; start_y-=1; end_x -= 1; end_y -= 1

ghost_list = []

for i in range(n):
    tmp = list(input())
    house.append(tmp)
    for j in range(m):
        if tmp[j] in ('0','1','2','3'):
            ghost_list.append((i,j))

ghost_zone = [[[False]*m for _ in range(n)]for _ in range(4)]

def find_ghost_view(graph,ghost_zone,start,move,time):
    x,y = start
    dx, dy = move
    while True:
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] != '.':
            return
        ghost_zone[time][x][y] = True

def find_ghost_zone(graph,ghost_zone,ghost_list):
    for ghost in ghost_list:
        ghost_x, ghost_y = ghost
        for i in range(4):
            d = (int(graph[ghost_x][ghost_y]) + i) % 4
            if d == 0:
                find_ghost_view(graph,ghost_zone,ghost,(0,1),i)
            elif d == 1:
                find_ghost_view(graph,ghost_zone,ghost,(1,0),i)
            elif d == 2:
                find_ghost_view(graph,ghost_zone,ghost,(0,-1),i)
            else:
                find_ghost_view(graph,ghost_zone,ghost,(-1,0),i)

def move_seokjoon(graph,visited,start,ghost_zone):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] != '.':
                continue
            for k in range(1,5):
                if ghost_zone[(visited[vx][vy]+k)%4][nx][ny] == False and visited[nx][ny] > visited[vx][vy] + k:
                    visited[nx][ny] = visited[vx][vy] + k
                    queue.append((nx,ny))
                    break
                if ghost_zone[(visited[vx][vy]+k)%4][vx][vy] == True:
                    break

INF = int(1e9)

visited = [[INF]*m for _ in range(n)]

find_ghost_zone(house,ghost_zone,ghost_list)
move_seokjoon(house,visited,(start_x,start_y),ghost_zone)

answer = visited[end_x][end_y]

if answer == INF:
    answer = 'GG'

print(answer)
