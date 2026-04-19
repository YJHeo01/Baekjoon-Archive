from collections import deque
import sys

input = sys.stdin.readline

r,c = map(int,input().split())

ground = []

for _ in range(r):
    ground.append(list(input()))

visited = [[False]*c for _ in range(r)]

def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    wolf = 0
    sheep = 0
    visited[start[0]][start[1]] = True
    while queue:
        vx,vy = queue.popleft()
        if graph[vx][vy] == 'v':
            wolf += 1
        elif graph[vx][vy] == 'k':
            sheep += 1
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] == '#':
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
    if wolf >= sheep:
        return wolf
    else:
        return -sheep

wolf, sheep = 0,0

for i in range(r):
    for j in range(c):
        if visited[i][j] == True or ground[i][j] == '#':
            continue
        tmp = bfs(ground,visited,(i,j))
        if tmp > 0:
            wolf += tmp
        else:
            sheep -= tmp

print(sheep,wolf)