from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int,input().split())
INF = int(1e9)
def bfs(graph,visited):
    queue = deque([(0,0)])
    visited[0][0] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        v = queue.popleft()
        vx, vy = v[0], v[1]
        for i in range(4):
            nx, ny = vx + dx[i], vy + dy[i]
            if nx >= n or nx < 0 or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                if visited[nx][ny] > visited[vx][vy] + 1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
array = [[0]*m for _ in range(n)]
block = []
visited = [[INF]*m for _ in range(n)]
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == '1':
            block.append((i,j))
            array[i][j] = 1
answer = INF
for point in block:
    array[point[0]][point[1]] = 0
    bfs(array,visited)
    answer = min(answer,visited[n-1][m-1])
    array[point[0]][point[1]] = 1
    visited = [[INF]*m for _ in range(n)]
if answer == INF:
    answer = -1
print(answer)