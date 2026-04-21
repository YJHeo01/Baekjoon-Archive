from collections import deque

n = int(input())

sea = []
shark_point = [-1,-1]
fish_cnt = 0

for i in range(n):
    tmp  = list(map(int,input().split()))
    sea.append(tmp)
    for j in range(n):
        if tmp[j] == 0:
            continue
        elif tmp[j] == 9:
            shark_point = (i,j)
        else:
            fish_cnt += 1

answer = 0
INF = 1000

def bfs(graph,visited,start):
    queue = deque([start])
    shortest_point = (-1,-1)
    shortest_distance = INF
    graph[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] > shark_size:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
                if graph[nx][ny] != 0 and shark_size > graph[nx][ny]:
                    if shortest_distance > visited[nx][ny]:
                        shortest_distance = visited[nx][ny]
                        shortest_point = (nx,ny)
                    elif shortest_distance == visited[nx][ny]:
                        if nx < shortest_point[0] or (nx == shortest_point[0] and ny < shortest_point[1]):
                            shortest_point = (nx,ny)
    return shortest_point

answer = 0
shark_size = 2
level_up_cnt = 0
for i in range(fish_cnt):
    distance = [[INF]*n for _ in range(n)]
    shark_point = bfs(sea,distance,shark_point)
    if shark_point == (-1,-1):
        break
    x,y = shark_point
    level_up_cnt += 1
    if level_up_cnt == shark_size:
        level_up_cnt = 0
        shark_size += 1
    answer += distance[x][y]

print(answer)