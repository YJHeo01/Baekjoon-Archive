from collections import deque

n,m = map(int,input().split())

sea = []

for _ in range(n):
    sea.append(list(input()))

answer = [0] * (m+1)

check_island = [[False]*m for _ in range(n)]

def get_island_area(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    visited[start[0]][start[1]] = True
    ret_value = []
    while queue:
        vx,vy = queue.popleft()
        correct_ret_value = False
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == '.':
                correct_ret_value = True
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
        if correct_ret_value == True:
            ret_value.append((vx,vy))
    return ret_value

INF = int(1e9)

def get_height(graph,visited,start):
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = INF
    while queue:
        vx, vy = queue.popleft()
        if visited[vx][vy] >= ret_value:
            continue
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                ret_value = visited[vx][vy]
                continue
            if graph[nx][ny] == graph[vx][vy]:
                if visited[nx][ny] > visited[vx][vy]:
                    visited[nx][ny] = visited[vx][vy]
                    queue.append((nx,ny))
            else:
                if visited[nx][ny] > visited[vx][vy] + 1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
    if ret_value != 0:
        ret_value -= 1
    return ret_value

for i in range(n):
    for j in range(m):
        if sea[i][j] == 'x' and check_island[i][j] == False:
            island_area = get_island_area(sea,check_island,(i,j))
            visited_island_cnt = [[INF]*m for _ in range(n)]
            height = get_height(sea,visited_island_cnt,island_area)
            answer[height] += 1

answer.reverse()

start_idx = 0
for i in range(m+1):
    if answer[start_idx] != 0:
        break
    start_idx += 1
if start_idx > m:
    print(-1)
else:
    for i in range(start_idx,m+1):
        if answer[i] == 0:
            if sum(answer[i:]) == 0:
                break
        print(answer[i],end=" ")