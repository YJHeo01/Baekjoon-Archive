from collections import deque
import sys
mod = 10000000
input = sys.stdin.readline
n, m = map(int,input().split())
INF = 99999999

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
                if visited[nx][ny] == -1 or visited[nx][ny]> (visited[vx][vy] + 1):
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))

def bfs_plus_block(graph,visited):
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
                if visited[nx][ny] == -1 or visited[nx][ny] % mod > (visited[vx][vy] + 1) % mod:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
            else:
                if visited[vx][vy] > mod:
                    continue
                if visited[nx][ny] == -1 or visited[nx][ny] % mod > (visited[vx][vy] + 1) % mod:
                    visited[nx][ny] = visited[vx][vy] + 1 + mod
                    queue.append((nx,ny))


array = [[0]*m for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == '1':
            array[i][j] = 1

bfs(array,visited)
bfs_plus_block(array,visited)
if visited[n-1][m-1] == -1:
    print("-1")
else:
    print(visited[n-1][m-1]%mod)