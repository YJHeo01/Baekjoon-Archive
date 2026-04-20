from collections import deque

r,c = map(int,input().split())
INF = int(1e9)
ICE = 'X'
SWAN = 'L'
lake = []
melt_ice_day = [[INF]*c for _ in range(r)]
start = (-1,-1)
end = (-1,-1)

for i in range(r):
    tmp = list(input())
    lake.append(tmp)
    for j in range(c):
        if tmp[j] != ICE:
            melt_ice_day[i][j] = 0
            if tmp[j] == SWAN:
                if start == (-1,-1):
                    start = (i,j)
                else:
                    end = (i,j)

def check_edge(graph,point):
    x,y = point
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if graph[nx][ny] == ICE:
            return True
    return False

def BFS_check_melt_ice_day(visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
            
for i in range(r):
    for j in range(c):
        if lake[i][j] != ICE and check_edge(lake,(i,j)) == True:
            BFS_check_melt_ice_day(melt_ice_day,(i,j))

visited_day = [[INF]*c for _ in range(r)]

def solution(melt_day,visited_day,start):
    queue = deque([start])
    visited_day[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if visited_day[nx][ny] > max(visited_day[vx][vy],melt_day[nx][ny]):
                visited_day[nx][ny] = max(visited_day[vx][vy],melt_day[nx][ny])
                queue.append((nx,ny))

solution(melt_ice_day,visited_day,start)

print(visited_day[end[0]][end[1]])