from collections import deque

import sys

input = sys.stdin.readline

ground = []

r,c = map(int,input().split())
jihoon = (0,0)
fire = []
start = (0,0)

for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == '.' or tmp[j] == '#':
            continue
        elif tmp[j] == 'F':
            fire.append((i,j))
        else:
            jihoon = (i,j)
    ground.append(tmp)
INF = int(1e9)
visited = [[INF]*c for _ in range(r)]

def fire_move(graph,visited,start):
    queue = deque(start)
    for point in start:
        visited[point[0]][point[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >c:
                continue
            if graph[nx][ny] != '#' and visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

fire_move(ground,visited,fire)

def jihoon_move(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] != '#':
                if (nx == 0 or ny == 0 or nx == r-1 or ny == c-1) and visited[nx][ny] >= visited[vx][vy] + 1:
                    return visited[vx][vy] + 2
                if visited[nx][ny] > visited[vx][vy] + 1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
    return "IMPOSSIBLE" 

print(jihoon_move(ground,visited,jihoon))