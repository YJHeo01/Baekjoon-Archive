from collections import deque

n,m = map(int,input().split())

k,c = map(int,input().split())

graph = [list(input()) for _ in range(n)]

visited = [[[-1]*100 for _ in range(m)] for _ in range(n)]

start = (-1,-1)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            start = (i,j)
            
def bfs(graph,visited,start):
    start_x, start_y = start
    visited[start_x][start_y][0] = 0
    queue = deque([(start_x,start_y,0)])
    while queue:
        x,y,b = queue.popleft()
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0),(0,0)]:
            nx,ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == '#': continue
            if graph[nx][ny] == 'S' or graph[nx][ny] == 'H': nb = max(0,b-k)
            else: nb = min(100,b+c)
            if nb >= 100 or visited[nx][ny][nb] != -1: continue
            visited[nx][ny][nb] = visited[x][y][b] + 1
            queue.append((nx,ny,nb))

bfs(graph,visited,start)

answer = int(1e18)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'E':
            target_x, target_y = i,j
            break


for i in range(100):
    if visited[target_x][target_y][i] == -1: continue
    answer = min(answer,visited[target_x][target_y][i])

if answer >= int(1e18): answer = -1

print(answer)