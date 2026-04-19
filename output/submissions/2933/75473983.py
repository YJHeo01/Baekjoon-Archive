from collections import deque

r,c = map(int,input().split())

graph = []

INF = int(1e9)

for _ in range(r):
    graph.append(list(input()))

n = int(input())

def search_cluster(graph,visited,start):
    queue = deque([start])
    idx = visited[start[0]][start[1]]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == 'x' and visited[nx][ny] == 0:
                visited[nx][ny] = idx
                queue.append((nx,ny))

def search_second_cluster_dx(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    ret_value = INF
    while queue:
        vx,vy = queue.popleft()
        nx = vx + dx[0]
        ny = vy + dy[0]
        if nx == r:
            ret_value = min(ret_value,visited[vx][vy])
        elif graph[nx][ny] == 1:
            visited[nx][ny] = visited[vx][vy] + 1
            ret_value = min(ret_value,visited[vx][vy])
        else:
            if visited[nx][ny] > visited[vx][vy] + 1:
                queue.append((nx,ny))
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[vx][vy] + 1
                else:
                    visited[nx][ny] = 0
        if graph[vx][vy] == 2:
            for i in range(1,4):
                nx = vx + dx[i]
                ny = vy + dy[i]
                if nx < 0 or ny < 0 or ny >= c:
                    continue
                if visited[nx][ny] > visited[vx][vy] + 1 and graph[nx][ny] == 2:
                    visited[nx][ny] = 0
                    queue.append((nx,ny))
    return ret_value 
        
def search_second_cluster_area(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = True
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == 2 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))

def move_second_cluster(graph,second_cluster_area,dx):
    for i in range(r):
        for j in range(c):
            if second_cluster_area[i][j] == True:
                graph[i][j] = '.'
    for i in range(r-dx):
        for j in range(c):
            if second_cluster_area[i][j] == True:
                graph[i+dx][j] = 'x'
        
command = list(map(int,input().split()))
for idx in range(n):
    h = command[idx]
    w = -1
    if idx % 2 == 0:
        for i in range(c):
            if graph[r-h][i] == 'x':
                w = i
                break
    else:
        for i in range(c-1,-1,-1):
            if graph[r-h][i] == 'x':
                w = i
                break
    if w == -1:
        continue
    graph[r-h][w] = '.'
    cluster_cnt = 0
    cluster_point = []
    cluster_idx = [[0]*c for _ in range(r)]
    for i in range(min(r-h+1,r-1),r):
        for j in range(c):
            if graph[i][j] == 'x' and cluster_idx[i][j] == 0:
                cluster_cnt = 1
                cluster_idx[i][j] = cluster_cnt
                search_cluster(graph,cluster_idx,(i,j))
                cluster_point.append((i,j))
    for i in range(r-h):
        for j in range(c):
            if graph[i][j] == 'x' and cluster_idx[i][j] == 0:
                cluster_cnt = 2
                cluster_idx[i][j] = cluster_cnt
                search_cluster(graph,cluster_idx,(i,j))
                cluster_point.append((i,j))
                break
    if cluster_cnt >= 2:
        visited = [[INF]*c for _ in range(r)]
        dx = search_second_cluster_dx(cluster_idx,visited,cluster_point[-1])
        second_cluster_area = [[False]*c for _ in range(r)]
        search_second_cluster_area(cluster_idx,second_cluster_area,cluster_point[-1])
        move_second_cluster(graph,second_cluster_area,dx)

for i in range(r):
    for j in range(c):
        print(graph[i][j],end="")
    print()