from collections import deque

n,m = map(int,input().split())

array = []

for _ in range(n):
    array.append(list(input()))

INF = int(1e9)

def bfs(graph,crash_block):
    queue = deque([(0,0)])
    graph[crash_block[0]][crash_block[1]] = '0'
    visited = [[INF]*m for _ in range(n)]
    visited[0][0] = 1
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx, ny = vx + dx[i], vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == '0' and visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    graph[crash_block[0]][crash_block[1]] = '1'
    return visited[n-1][m-1]
answer = bfs(array,(0,0))    
for i in range(n):
    for j in range(m):
        if array[i][j] == '1':
           answer = min(answer,bfs(array,(i,j)))
if answer == INF:
    answer = -1
print(answer)