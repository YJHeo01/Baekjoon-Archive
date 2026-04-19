from collections import deque

n,m = map(int,input().split())

sea = []

for _ in range(n):
    sea.append(list(map(int,input().split())))

node_idx = 2
node_position = [(-1,-1),(-1,-1)]
def search_node_idx(graph,start):
    queue = deque([start])
    idx = graph[start[0]][start[1]]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = idx
                queue.append((nx,ny))

for i in range(n):
    for j in range(n):
        if sea[i][j] == 1:
            sea[i][j] = node_idx
            node_position.append([i,j])
            search_node_idx(sea,(i,j))
            node_idx += 1

edges = []

INF = int(1e9)

def search_edge(graph,visited,start):
    distance = [INF] * node_idx
    start_idx = graph[start[0]][start[1]]
    queue = deque([start+[0]])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    distance[start_idx] = 0
    while queue:
        vx,vy,d = queue.popleft()
        if graph[vx][vy] == start_idx:
            for i in range(4):
                nx = vx + dx[i]
                ny = vy + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] > visited[vx][vy] + 1:
                    if graph[nx][ny] == start_idx:
                        visited[nx][ny] = 0
                    else:
                        visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny,i))
        else:
            nx = vx + dx[d]
            ny = vy + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                if graph[nx][ny] == start_idx:
                    continue
                elif graph[nx][ny] > 0:
                    if visited[vx][vy] >= 2:
                        new_island_idx = graph[nx][ny]
                        distance[new_island_idx] = min(distance[new_island_idx],visited[vx][vy])
                else:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny,d))
    return distance

for i in range(2,node_idx):
    visited = [[INF]*m for _ in range(n)]
    distance = search_edge(sea,visited,node_position[i])
    for j in range(i+1,node_idx):
        edges.append((distance[j],i,j))

parent = [0] * node_idx

for i in range(2,node_idx):
    parent[i] = i

edges.sort()

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0

for edge in edges:
    distance, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        answer += distance
        if answer >= INF:
            answer = -1
            break
        union_parent(parent,a,b)

print(answer)