from collections import deque

n = int(input())
INF = int(1e9)
graph = [[0]*501 for _ in range(501)]
visited = [[INF]*501 for _ in range(501)]
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    if x1 > x2 :
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for j in range(x1,x2+1):
        for k in range(y1,y2+1):
            graph[j][k] = 1
n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    if x1 > x2 :
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for j in range(x1,x2+1):
        for k in range(y1,y2+1):
            graph[j][k] = 2

queue = deque([(0,0)])
visited[0][0] = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

while queue:
    vx, vy = queue.popleft()
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx > 500 or ny > 500:
            continue
        if graph[nx][ny] == 0: 
            if visited[nx][ny] > visited[vx][vy]:
                visited[nx][ny] = visited[vx][vy]
                queue.append((nx,ny))
        elif graph[nx][ny] == 1:
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

if visited[500][500] == INF:
    print(-1)
else:
    print(visited[500][500])