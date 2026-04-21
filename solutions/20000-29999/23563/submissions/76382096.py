from collections import deque

h,w = map(int,input().split())

maze = []

for _ in range(h):
    maze.append(list(input()))

start = (-1,-1)
end = (-1,-1)

for i in range(h):
    for j in range(w):
        if maze[i][j] == 'S':
            start = (i,j)
        elif maze[i][j] == 'E':
            end = (i,j)

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
            if i <= 1:
                if (graph[vx+1][vy] == '#' and graph[nx+1][ny] == '#') or (graph[vx-1][vy] == '#' and graph[nx-1][ny] == '#'):
                    if visited[nx][ny] > visited[vx][vy]:
                        visited[nx][ny] = visited[vx][vy]
                        queue.append((nx,ny))
                else:
                    if visited[nx][ny] > visited[vx][vy] + 1:
                        visited[nx][ny] = visited[vx][vy] + 1
                        queue.append((nx,ny))
            else:
                if (graph[vx][vy+1] == '#' and graph[nx][ny+1] == '#') or (graph[vx][vy-1] == '#' and graph[nx][ny-1] == '#'):
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