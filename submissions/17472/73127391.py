from collections import deque

n,m = map(int,input().split())

country = []

for _ in range(n):
    country.append(list(map(int,input().split())))
next_idx = 2
def check_island_idx(graph,start,new_idx):
    queue = deque([start])
    graph[start[0]][start[1]] = new_idx
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
                graph[nx][ny] = new_idx
                queue.append((nx,ny))
    
for i in range(n):
    for j in range(m):
        if country[i][j] == 1:
            check_island_idx(country,(i,j),next_idx)
            next_idx += 1


parent = [0] * (next_idx)

for i in range(2,next_idx):
    parent[i] = i

bridge_list = []

def find_bridge(start):
    dx = [0,1]
    dy = [1,0]
    ret_value = []
    for i in range(2):
        x,y = start
        length = 0
        while True:
            x += dx[i]
            y += dy[i]
            if x >= n or y >= m:
                break
            if country[x][y] != 0:
                if country[x][y] != country[start[0]][start[1]] and length >= 2:
                    ret_value.append((length,country[x][y],country[start[0]][start[1]]))
                break
            length += 1
    return ret_value

for i in range(n):
    for j in range(m):
        if country[i][j] != 0:
            bridge_list += find_bridge((i,j))

bridge_list.sort()

answer = 0

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

connect_island = [False] * next_idx
for bridge in bridge_list:
    length,a,b = bridge
    if find_parent(parent,a) != find_parent(parent,b):
        connect_island[a] = True
        connect_island[b] = True
        union_parent(parent,a,b)
        answer += length

for i in range(2,next_idx):
    if connect_island[i] == False:
        answer = -1
        break
print(answer)