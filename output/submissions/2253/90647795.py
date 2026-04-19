from collections import deque

import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

block = [False] * (n+1)

for _ in range(m):
    block[int(input())] = True

visited = [[INF]*1000 for _ in range(n+1)]

visited[1][0] = 0

queue = deque([(1,0)])

while queue:
    vx, jump = queue.popleft()
    for i in [1,0,-1]:
        dx = jump + i
        if dx <= 0 or dx >= 2000: continue
        nx = vx + dx
        if nx > n or block[nx] or visited[nx][dx] != INF: continue
        visited[nx][dx] = visited[vx][jump] + 1
        queue.append((nx,dx))
        
answer = min(visited[n])

if answer >= INF: answer = -1

print(answer)