from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

def bfs(graph,start):
    queue = deque([start])
    graph[start[0]][start[1]] = 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            nx %= n; ny %= m
            if graph[nx][ny] == 1: continue
            graph[nx][ny] = 1
            queue.append((nx,ny))
            
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: continue
        answer += 1
        bfs(graph,(i,j))
        
print(answer)