from collections import deque

n,m = map(int,input().split())

sea = []

for _ in range(n):
    sea.append(list(input()))

island_cnt = 0

def search_island_area(graph,start,idx):
    queue = deque([start])
    dx = [0,1,0,-1,1,-1,1,-1]
    dy = [1,0,-1,0,1,1,-1,-1]
    graph[start[0]][start[1]] = idx
    max_x,min_x = start[0],start[0]
    max_y,min_y = start[1],start[1]
    while queue:
        vx,vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'x':
                max_x, min_x, max_y, min_y = max(max_x,nx),min(min_x,nx),max(max_y,ny),min(min_y,ny)
                graph[nx][ny] = idx
                queue.append((nx,ny))
    return start,max_x,min_x,max_y,min_y
island_point, max_x_list, min_x_list, max_y_list, min_y_list = [],[],[],[],[]

for i in range(n):
    for j in range(m):
        if sea[i][j] == 'x':
            tmp1,tmp2,tmp3,tmp4,tmp5 = search_island_area(sea,(i,j),island_cnt)
            island_point.append(tmp1)
            max_x_list.append(tmp2)
            min_x_list.append(tmp3)
            max_y_list.append(tmp4)
            min_y_list.append(tmp5)
            island_cnt += 1

island_high = [0] * island_cnt
max_high = 0

def escape_route(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = True
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                return True
            if visited[nx][ny] == False:
                if graph[nx][ny] == '.' or graph[nx][ny] == graph[start[0]][start[1]]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return False

graph = [[] for _ in range(island_cnt)]
zero_high = [True] * (island_cnt)

for i in range(island_cnt):
    for j in range(island_cnt):
        if max_x_list[i] > max_x_list[j] and min_x_list[i] < min_x_list[j] and min_y_list[i] < min_y_list[j] and max_y_list[i] > max_y_list[j]:
            visited = [[False]*m for _ in range(n)]
            if escape_route(sea,visited,island_point[j]) == False:
                graph[j].append(i)
                zero_high[i] = False

def find_island_high(graph,visited,start):
    queue = deque([start])
    while queue:
        idx = queue.popleft()
        for next_idx in graph[idx]:
            visited[next_idx] = max(visited[next_idx],visited[idx]+1)

if island_cnt == 0:
    print(-1)
else:
    high_list = [0] * island_cnt
    for i in range(island_cnt):
        if zero_high[i] == True:
            find_island_high(graph,high_list,i)
    answer = [0] * (max(high_list)+1)
    for high in high_list:
        answer[high] += 1
    for i in answer:
        print(i,end=" ")