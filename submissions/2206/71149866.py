#https://github.com/YJHeo01
from collections import deque

n,m = map(int,input().split())

array = []

for _ in range(n):
    array.append(list(input()))

INF = int(1e9)

visited = [[INF]*m for _ in range(n)]

def search_distance_start_to_block_and_dest(graph,visited,start):
    queue = deque([start])
    visited[0][0] = 1
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx, ny = vx + dx[i], vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                if graph[nx][ny] == '0': 
                    queue.append((nx,ny))
    return visited[n-1][m-1]

def search_distance_block_to_destination(graph,visited,start):
    queue = deque([start])
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
    return visited[n-1][m-1]

answer = search_distance_start_to_block_and_dest(array,visited,(0,0))
for i in range(n):
    for j in range(m):
        if array[i][j] == '1' and visited[i][j] != INF:
           answer = min(answer,search_distance_block_to_destination(array,visited,(i,j)))
if answer == INF:
    answer = -1
print(answer)