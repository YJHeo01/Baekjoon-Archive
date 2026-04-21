from collections import deque

n,m,k = map(int,input().split())

ground = [[0]*(m+1) for _ in range(n+1)]
visited = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    r,c = map(int,input().split())
    ground[r][c] = 1

def measure_trash_size(graph, visited,start):
    ret_value = 1
    visited[start[0]][start[1]] = 1
    queue = deque([start])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                ret_value += 1
    return ret_value

answer = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if visited[i][j] == 0 and ground[i][j] == 1:
            answer = max(answer,measure_trash_size(ground,visited,(i,j)))

print(answer)