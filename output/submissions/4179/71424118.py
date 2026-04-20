#https://github.com/YJHeo01

from collections import deque
import sys

input = sys.stdin.readline

r,c = map(int,input().split())

ground = []
jihoon = 0
fire = []
INF = int(1e9)
visited = [[INF] * c for _ in range(r)]
for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == 'F':
            visited[i][j] = 1
            fire.append((i,j))
        elif tmp[j] == 'J':
            visited[i][j] = 1
            jihoon = (i,j)
    ground.append(tmp)



def move_fire(graph,visited,start):
    queue = deque(start)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == '#':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    
move_fire(ground,visited,fire)

def move_jihoon(graph,visited,start):
    ret_value = INF
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] != '#' and visited[nx][ny] > visited[vx][vy] + 1:
                if nx == 0 or ny == 0 or nx == r-1 or ny == c-1:
                    ret_value = min(ret_value, visited[vx][vy] + 1)
                else:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
    return ret_value

answer = move_jihoon(ground,visited,jihoon)
if answer == INF:
    answer = "IMPOSSIBLE"
print(answer)