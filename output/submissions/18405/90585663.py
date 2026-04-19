from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int,input().split())

INF = int(1e9)

arr = [list(map(int,input().split())) for _ in range(n)]

start = [[] for _ in range(k)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0: continue
        start[arr[i][j]-1].append((i,j))


s, target_x, target_y = map(int,input().split())
target_x -= 1; target_y -= 1
    
dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 0
answer_dist = INF

for i in range(1,k+1):
    queue = deque(start[i-1])
    visited = [[INF]*n for _ in range(n)]
    for x,y in start[i-1]:
        visited[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] != INF: continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))
    dist = visited[target_x][target_y]
    if dist <= s and answer_dist > dist:
        answer = i
        answer_dist = dist

print(answer)