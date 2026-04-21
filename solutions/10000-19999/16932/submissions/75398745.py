from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int,input().split())))

area_max_idx = 2


def bfs(graph,start,idx):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    graph[start[0]][start[1]] = idx
    ret_value = 1
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
                ret_value += 1
    return ret_value

area_size = [0,0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            area_size.append(bfs(matrix,(i,j),area_max_idx))
            area_max_idx += 1

answer = 1

for x in range(n):
    for y in range(m):
        if matrix[x][y] == 0:
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
            check_area = [False] * area_max_idx
            tmp = 1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                area_idx = matrix[nx][ny]
                if check_area[area_idx] == False:
                    check_area[area_idx] = True
                    tmp += area_size[area_idx]
            answer = max(answer,tmp)

print(answer)