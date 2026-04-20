import sys

input = sys.stdin.readline

from collections import deque

r, c = map(int,input().split())

ground = []

for _ in range(r):
    ground.append(list(input()))

visited = [[False]*c for _ in range(r)]

def check_sheep_wolf(graph,visited,start):
    queue = deque([start])
    move_type = [(0,1),(1,0),(-1,0),(0,-1)]
    sheep_cnt,wolf_cnt = 0,0
    visited[start[0]][start[1]] = True
    if graph[start[0]][start[1]] != '.':
        if graph[start[0]][start[1]] == 'v':
            wolf_cnt += 1
        else:
            sheep_cnt += 1
    while queue:
        vx, vy = queue.popleft()
        for move in move_type:
            nx = vx + move[0]
            ny = vy + move[1]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] != '#' and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
                if graph[nx][ny] == 'o':
                    sheep_cnt += 1
                elif graph[nx][ny] == 'v':
                    wolf_cnt += 1
    if wolf_cnt >= sheep_cnt:
        return (0,wolf_cnt)
    else:
        return (sheep_cnt,0)

sheep = 0
wolf = 0

for i in range(r):
    for j in range(c):
        if ground[i][j] != '#' and visited[i][j] ==False:
            result = check_sheep_wolf(ground,visited,(i,j))
            sheep += result[0]
            wolf += result[1]

print(sheep,wolf)