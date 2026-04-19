from collections import deque

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        graph[i][j] = int(graph[i][j])

def check_make_new_pool(graph,visited,start,height):
    ret_value = True
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = True
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                ret_value = False
                continue
            if graph[nx][ny] < height and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return ret_value

def build_new_pool(graph,visited,start,height):
    queue = deque([start])
    ret_value = 1
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    graph[start[0]][start[1]] += 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if height > graph[nx][ny] and visited[nx][ny] == False:
                ret_value += 1
                visited[nx][ny] = True
                graph[nx][ny] += 1
                queue.append((nx,ny))
    return ret_value

answer = 0

for height in range(2,10):
    visited = [[False]*m for _ in range(n)]
    pool_zone = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if visited[x][y] == True or graph[x][y] >= height:
                continue
            if check_make_new_pool(graph,visited,(x,y),height) == True:
                make_new_pool = True
                answer += build_new_pool(graph,pool_zone,(x,y),height)
    
print(answer)