from collections import deque

h,w = map(int,input().split())

maze = []

for _ in range(h):
    maze.append(list(input()))

start = (-1,-1)
end = (-1,-1)

for x in range(1,h-1):
    for y in range(1,w-1):
        if maze[x][y] == 'S':
            start = (x,y)
        if maze[x][y] == 'E':
            end = (x,y)

        if maze[x][y] != '#':
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
            adj = False
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if maze[nx][ny] == '#':
                    adj = True
                    break
            if adj == True:
                maze[x][y] = 'a'
        else:
            continue

INF = int(1e9)

visited = [[INF]*w for _ in range(h)]

def solution(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '#':
                continue
            if graph[nx][ny] == 'a' and graph[vx][vy] == 'a':
                if visited[nx][ny] > visited[vx][vy]:
                    visited[nx][ny] = visited[vx][vy]
                    queue.append((nx,ny))
            else:
                if visited[nx][ny] > visited[vx][vy] + 1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))

solution(maze,visited,start)

answer = visited[end[0]][end[1]]

print(answer)