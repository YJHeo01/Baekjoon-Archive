from collections import deque


INF = int(1e9)

answer = 0

h, w = map(int,input().split())

def bfs(graph,visited,start):
    global answer
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        v = queue.popleft()
        vx, vy = v[0],v[1]
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == 'W':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy]+1
                answer = max(visited[nx][ny],answer)
                queue.append((nx,ny))



ground = []
for i in range(h):
    tmp = list(input())
    ground.append(tmp)


for i in range(h):
    for j in range(w):
        if ground[i][j] == 'L':
            visited = [[INF] * w for _ in range(h)]
            bfs(ground,visited,(i,j))

print(answer)