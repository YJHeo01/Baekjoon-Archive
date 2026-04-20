from collections import deque

m,n = map(int,input().split())

factory = []

for _ in range(m):
    factory.append(list(map(int,input().split())))

start_row, start_column, start_direction = map(int,input().split())
dest_row, dest_column, dest_direction = map(int,input().split())

def change_direction_value(value):
    if value == 4:#북
        return 2
    elif value == 1:#동
        return 1
    elif value == 3:#남
        return 0
    else:#서
        return 3
    
start_row-=1; start_column-=1; dest_row-=1; dest_column-=1
start_direction, dest_direction = change_direction_value(start_direction),change_direction_value(dest_direction)

INF = int(1e9)

visited = [[[INF]*n for _ in range(m)]for _ in range(4)]

def move_robot(graph,visited):
    queue = deque([(start_row,start_column,start_direction)])
    visited[start_direction][start_row][start_column] = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while queue:
        vx, vy, vd = queue.popleft()
        # Command 1 : Go k``
        for k in range(1,4):
            nx = vx + dx[vd] * k
            ny = vy + dy[vd] * k
            if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[nx][ny] == 1:
                break
            if visited[vd][nx][ny] > visited[vd][vx][vy] + 1:
                visited[vd][nx][ny] = visited[vd][vx][vy] + 1
                queue.append((nx,ny,vd))

        #Command 2 : Turn dir
        for i in [1,-1]: 
            nd = (vd + i) % 4
            if visited[nd][vx][vy] > visited[vd][vx][vy] + 1:
                visited[nd][vx][vy] = visited[vd][vx][vy] + 1
                queue.append((vx,vy,nd))

move_robot(factory,visited)

print(visited[dest_direction][dest_row][dest_column])