from collections import deque

n = int(input())

town = [list(input()) for _ in range(n)]

high = [list(map(int,input().split())) for _ in range(n)]

start = (-1,-1)

for i in range(n):
    for j in range(n):
        if town[i][j] == 'P': start = (i,j)

INF = 1000000

start_high = high[start[0]][start[1]]

def bfs(graph,visited,start,min_high,max_high):
    queue = deque([start])
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    while queue:
        vx,vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] < min_high or graph[nx][ny] > max_high: continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))

min_high_limit = start_high
max_high_limit = start_high

target = []

for i in range(n):
    for j in range(n):
        if town[i][j] == 'K':
            target.append((i,j))
            min_high_limit = min(min_high_limit,high[i][j])
            max_high_limit = max(max_high_limit,high[i][j])

answer = INF

for min_high in range(min_high_limit+1):
    left, right = max_high_limit, min(min_high+answer,INF)
    while left <= right:
        max_high = (left+right) // 2
        visited = [[False]*n for _ in range(n)]
        bfs(high,visited,start,min_high,max_high)
        complete = True
        for x,y in target:
            if visited[x][y] == False:
                complete = False
                break
        if complete:
            answer = min(answer,max_high-min_high)
            right = max_high - 1
        else:
            left = max_high + 1

print(answer)