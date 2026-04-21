from collections import deque
import sys

input = sys.stdin.readline
r,c = map(int,input().split())

array = []

fire = []
jihoon = (-1,-1)

for i in range(r):
    tmp = list(input())
    array.append(tmp)
    for j in range(c):
        if tmp[j] == 'J':
            jihoon = (i,j)
        elif tmp[j] == 'F':
            fire.append((i,j))

INF = int(1e9)

visited = [[INF]*c for _ in range(r)]

def move_fire(graph,visited,start):
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] == '#':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

move_fire(array,visited,fire)

def move_jihoon(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if graph[nx][ny] == '#':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                if nx == 0 or ny == 0 or nx == r-1 or ny == c-1:
                    return visited[vx][vy] + 2
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    return "IMPOSSIBLE"

answer = move_jihoon(array,visited,jihoon)

print(answer)