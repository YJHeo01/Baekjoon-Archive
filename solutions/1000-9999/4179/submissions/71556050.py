from collections import deque

r,c = map(int,input().split())

ground = []

fire = []
jihoon = (-1,-1)

for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == 'F':
            fire.append((i,j))
        elif tmp[j] == 'J':
            jihoon = (i,j)
    ground.append(tmp)

def move_fire(graph,visited,start):
    queue = deque(start)
    for point in start:
        visited[point[0]][point[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] != '#' and visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
        
INF = int(1e9)
visited = [[INF]*c for _ in range(r)]

move_fire(ground,visited,fire)

def move_jihoon(graph,visited,start):
    answer = "IMPOSSIBLE"
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if graph[nx][ny] == '#':
                continue
            if nx == 0 or ny == 0 or nx == r-1 or ny == c-1:
                answer = visited[vx][vy] + 2
                return answer
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

print(move_jihoon(ground,visited,jihoon)) 