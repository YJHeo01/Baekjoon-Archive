from collections import deque

import sys

INF = int(1e9)

input = sys.stdin.readline

n,m = map(int,input().split())

matrix = [list(input().rstrip()) for _ in range(n)]

visited = [[[INF]*2 for _ in range(m)] for _ in range(n)]

visited[0][0][0] = 1

queue = deque([(0,0,0)])

while queue:
    x,y,state = queue.popleft()
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
        next_state = state + int(matrix[nx][ny])
        if next_state >= 2 or visited[nx][ny][next_state] != INF: continue
        visited[nx][ny][next_state] = visited[x][y][state] + 1
        queue.append((nx,ny,next_state))

answer = min(visited[n-1][m-1])

if answer >= INF: answer = -1

print(answer)