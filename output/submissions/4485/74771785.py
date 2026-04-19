from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)

def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = graph[start[0]][start[1]]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] > visited[vx][vy] + graph[nx][ny]:
                visited[nx][ny] = visited[vx][vy] + graph[nx][ny]
                queue.append((nx,ny))
idx = 0

while True:
    n = int(input())
    if n == 0:
        break
    idx += 1
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    visited = [[INF]*n for _ in range(n)]
    bfs(graph,visited,(0,0))
    answer = visited[n-1][n-1]
    print("Problem " + str(idx) +": " + str(answer))