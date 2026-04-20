from collections import deque

n,m = map(int,input().split())
jump = [0] * 101
for i in range(n+m):
    x,y = map(int,input().split())
    jump[x] = y

visited = [0] * 101

def bfs(visited,jump,start):
    queue = deque([start])
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        for i in range(6,0,-1):
            nx = vx + i
            if nx > 100:
                continue
            if jump[nx] != 0:
                nx = jump[nx]
            if visited[nx] == 0 or visited[nx] > visited[vx] + 1:
                queue.append(nx)
                visited[nx] = visited[vx] + 1
bfs(visited,jump,1)

print(visited[100])