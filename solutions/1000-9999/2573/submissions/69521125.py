from collections import deque

n,m = map(int,input().split())

def bfs(graph,visited,start):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited[start[0]][start[1]] = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        vx = v[0]
        vy = v[1]
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] > 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

def melt(graph,points):
    ice_melt = []
    ret_v = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for point in points:
        tmp = 0
        for i in range(4):
            nx = point[0] + dx[i]
            ny = point[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] <= 0:
                tmp += 1
        ice_melt.append((point[0],point[1],tmp))
    for point in ice_melt:
        graph[point[0]][point[1]] -= point[2]
        if graph[point[0]][point[1]] > 0:
            ret_v.append((point[0],point[1]))
    return ret_v
        
                
sea = []
ice = []

for i in range(n):
    tmp = list(map(int,input().split()))
    sea.append(tmp)
    for j in range(m):
        if tmp[j] != 0:
            ice.append((i,j))

answer = 0
iceberg = 1
while iceberg:
    answer += 1
    ice = melt(sea,ice)
    iceberg = 0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and sea[i][j] > 0:
                bfs(sea,visited,(i,j))
                iceberg += 1
    if iceberg > 1:
        break

print(answer)