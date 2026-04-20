from collections import deque

m, n = map(int,input().split())

factory = []

for _ in range(m):
    factory.append(list(map(int,input().split())))

start_x, start_y, start_direction = map(int,input().split())
INF = int(1e9)

visited = [[[INF] * n for _ in range(m)] for _ in range(4)]

finish_x, finish_y, finish_direction = map(int,input().split())

def set_direction(direction):
    if direction == 4:
        return 0
    elif direction == 3:
        return 2
    elif direction == 2:
        return 3
    else:
        return 1

start_direction = set_direction(start_direction)
finish_direction = set_direction(finish_direction)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def change_direction(visited,point,change_value):
    if visited[(point[2]+change_value)%4][point[0]][point[1]] > visited[point[2]][point[0]][point[1]] + 1:
        visited[(point[2]+change_value)%4][point[0]][point[1]] = visited[point[2]][point[0]][point[1]] + 1
        return True
    return False


def solution(graph,visited,start):
    queue = deque([start])
    visited[start[2]][start[0]][start[1]] = 0
    while queue:
        point = queue.popleft()
        for i in range(-1,2):
            if change_direction(visited,point,i) == True:
                queue.append([point[0],point[1],(point[2] + i)%4])
        vx, vy, d = point
        for i in range(1,4):
            nx,ny = vx + dx[d] * i, vy + dy[d]*i
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                break
            if graph[nx][ny] == 1:
                break
            if visited[d][nx][ny] > visited[d][vx][vy] + i:
                visited[d][nx][ny] = visited[d][vx][vy] + 1
                queue.append([nx,ny,d])

solution(factory,visited,[start_x-1,start_y-1,start_direction])

print(visited[finish_direction][finish_x-1][finish_y-1])