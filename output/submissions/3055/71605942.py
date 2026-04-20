from collections import deque

r,c = map(int,input().split())

forest = []

water = []

start = (0,0)

for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == '*':
            water.append((i,j))
        elif tmp[j] == 'S':
            start = (i,j)
    forest.append(tmp)

def move_water(graph,visited,start):
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >=c:
                continue
            if graph[nx][ny] in ('.','S') and visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    return

INF = int(1e9)
visited = [[INF]*c for _ in range(r)]

move_water(forest,visited,water)

def solution(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == 'D':
                return visited[vx][vy] + 1
            if graph[nx][ny] == '.' and visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    return "KAKTUS"

print(solution(forest,visited,start))