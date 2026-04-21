from collections import deque

n = int(input())

sea = []

for _ in range(n):
    sea.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def find_island_group(start,island_number):
    queue = deque([start])
    y,x = start[0], start[1]
    sea[y][x] = island_number
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if sea[ny][nx] == 1:
                sea[ny][nx] = island_number
                queue.append((ny,nx))
    
island_number = 2
island_area = [[],[]]

def check_island_edge(point):
    global island_area
    y,x = point[0],point[1]
    edge = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or sea[ny][nx] != 0:
            continue
        edge = True
        break
    return edge
    
for i in range(n):
    for j in range(n):
        if sea[i][j] == 1:
            point = (i,j)
            island_area.append([])
            if check_island_edge(point) == True:
                island_area[island_number].append(point)
            find_island_group(point,island_number)
            island_number += 1
        else:
            if sea[i][j] != 0 and check_island_edge(point) == True:
                island_area[sea[i][j]].append(point)

INF = 10001

def find_shortest_path(start):
    ret_value = INF
    island_number = sea[start[0][0]][start[0][1]]
    queue = deque(start)
    visited = [[INF]*n for _ in range(n)]
    for point in start:
        visited[point[0]][point[1]] = 0
    while queue:
        vy,vx = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or sea[ny][nx] == island_number:
                continue
            if sea[ny][nx] == 0:
                if visited[ny][nx] > visited[vy][vx] + 1:
                    visited[ny][nx] = visited[vy][vx] + 1
                    queue.append((ny,nx))
            else:
                ret_value = min(ret_value,visited[vy][vx])
    return ret_value

answer = INF 

for i in range(2,island_number):
    answer = min(find_shortest_path(island_area[i]),answer)

print(answer)