from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

INF = int(1e9)

def fire_bfs(graph,visited,start):
    queue = deque(start)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for x,y in start:
        visited[x][y] = 0
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '#':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

def solution(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    while queue:
        vx, vy = queue.popleft()
        if vx == 0 or vy == 0 or vx == h-1 or vy == w-1:
            return visited[vx][vy] + 1
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '#':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    return "IMPOSSIBLE"

for _ in range(t):
    building = []
    w,h = map(int,input().split())
    visited = [[INF]*w for _ in range(h)]
    start = (-1,-1)
    fire = []
    for i in range(h):
        tmp = list(input())
        for j in range(w):
            if tmp[j] == '@':
                start = (i,j)
            elif tmp[j] == '*':
                fire.append((i,j))
            else:
                continue
        building.append(tmp)
    fire_bfs(building,visited,fire)
    print(solution(building,visited,start))