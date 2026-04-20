from collections import deque

n,m = map(int,input().split())

visited = [[-1]*(n+1) for _ in range(n+1)]

x,y = map(int,input().split())

queue = deque([(x,y)])

visited[x][y] = 0

while queue:
    x, y = queue.popleft()
    for dx,dy in [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]:
        nx,ny = x + dx, y + dy
        if nx > n or ny > n or nx <= 0 or ny <= 0: continue
        if visited[nx][ny] != -1: continue
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx,ny))
        
for _ in range(m):
    a,b = map(int,input().split())
    print(visited[a][b],end=" ")
    