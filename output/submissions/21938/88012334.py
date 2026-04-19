from collections import deque

n,m = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

t = int(input()) * 3

display = []

for i in range(n):
    tmp = []
    for j in range(m):
        if sum(data[i][3*j:3*j+3]) >= t:
            tmp.append(1)
        else:
            tmp.append(0)
    display.append(tmp)

answer = 0

visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j] or display[i][j] == 0: continue
        answer += 1
        queue = deque([(i,j)])
        visited[i][j] = True
        while queue:
            vx,vy = queue.popleft()
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny = vx + dx, vy + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
                if visited[nx][ny] == False and display[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

print(answer)