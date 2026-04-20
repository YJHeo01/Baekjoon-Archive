from collections import deque

m,n = map(int,input().split())

picture = []

for _ in range(m):
    picture.append(list(map(int,input().split())))

visited = [[False]*n for _ in range(m)]

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,-1,1,-1,1]
    while queue:
        vx, vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny <0 or nx >= m or ny>=n:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))


answer = 0
for i in range(m):
    for j in range(n):
        if picture[i][j] == 1 and visited[i][j] == False:
            answer += 1
            bfs(picture,visited,(i,j))

print(answer)