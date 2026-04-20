from collections import deque

n = int(input())
visited = [[0]*n for _ in range(n)]

def bfs(graph,rain,start):
    queue = deque([start])
    visited[start[0]][start[1]]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        v = queue.popleft()
        vx,vy = v[0],v[1]
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] > rain:
                visited[nx][ny] = 1
                queue.append((nx,ny))


space = []
rain_max = 0
rain_min = 101
for i in range(n):
    tmp = list(map(int,input().split()))
    rain_min = min(rain_min,min(tmp))
    rain_max = max(rain_max,max(tmp))
    space.append(tmp)
cnt = 0
for i in range(rain_min-1,rain_max):
    tmp = 0
    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0 and space[j][k] > i:
                bfs(space,i,(j,k))
                tmp += 1
    cnt = max(cnt,tmp)
    visited = [[0]*n for _ in range(n)]

print(cnt)