from collections import deque
import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(n)]

start = (-1,-1)

end = (-1,-1)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            graph[i][j] = '0'
            start = (i,j)
        if graph[i][j] == 'H':
            graph[i][j] = '0'
            end = (i,j)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = [[[-1]*4 for _ in range(m)] for _ in range(n)]

queue = deque()

start_x, start_y = start

for i in range(4):
    x = start_x + dx[(i+2) % 4]
    y = start_y + dy[(i+2) % 4]
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == 'X': continue
    visited[start_x][start_y][i] = 0
    queue.append((start_x,start_y,i))
    
while queue:
    x,y,d = queue.popleft()
    for i in range(4):
        if (d+2) % 4 == i: continue
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny][i] != -1 or graph[nx][ny] == 'X': continue
        last_x, last_y = x + dx[(d+2) % 4], y + dy[(d+2) % 4]
        if visited[x][y][d] == 0:
            if int(graph[nx][ny]) > k: continue
        else:        
            if int(graph[last_x][last_y]) + int(graph[x][y]) + int(graph[nx][ny]) > k: continue
        visited[nx][ny][i] = visited[x][y][d] + 1
        queue.append((nx,ny,i))
        
answer = int(1e9)

end_x, end_y = end
for i in range(4):
    if visited[end_x][end_y][i] == -1: continue
    answer = min(answer,visited[end_x][end_y][i])
    
if answer >= int(1e9): answer = -1

print(answer)