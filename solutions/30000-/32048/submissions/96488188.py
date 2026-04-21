from collections import deque

n = int(input())

visited = [[-1] * 2001 for _ in range(2001)]

queue = deque([(1000,1000)])

visited[1000][1000] = 0

while queue:
    x,y = queue.popleft()
    for dx,dy in [(0,1),(1,0),(1,-1),(0,-1),(-1,0),(-1,1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx > 2000 or ny > 2000: continue
        if visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))
            
for _ in range(n):
    i,j = map(int,input().split())
    print(visited[i+1000][j+1000])