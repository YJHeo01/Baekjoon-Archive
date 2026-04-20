from collections import deque

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] > visited[vx][vy]:
                if graph[nx][ny] == '1':
                    if visited[nx][ny] > visited[vx][vy] + 1:
                        visited[nx][ny] = visited[vx][vy] + 1
                        queue.append((nx,ny))
                else:
                    visited[nx][ny] = visited[vx][vy]
                    queue.append((nx,ny))
    return
                    


INF = int(1e9)

m,n = map(int,input().split())

ground = []

for _ in range(n):
    ground.append(list(input()))

visited = [[INF]*m for _ in range(n)]

bfs(ground,visited,(0,0))
print(visited[n-1][m-1])