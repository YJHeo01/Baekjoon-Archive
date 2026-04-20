from collections import deque
import sys

INF = int(1e9)

input = sys.stdin.readline

n,m = map(int,input().split())

x1,y1,x2,y2 = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(n)]

visited = [[INF]*m for _ in range(n)]

x1 -= 1; y1 -= 1; y2 -= 1; x2 -= 1

def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if graph[nx][ny] == '1':
                if visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
            else:
                if visited[nx][ny] > visited[x][y]:
                    visited[nx][ny] = visited[x][y]
                    queue.append((nx,ny))
    
visited[x1][y1] = 1

bfs(graph,visited,(x1,y1))

print(visited[x2][y2])