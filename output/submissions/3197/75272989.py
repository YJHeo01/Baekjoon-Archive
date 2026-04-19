from collections import deque
import sys

input = sys.stdin.readline

r,c = map(int,input().split())

lake = []

start = (-1,-1)
end = (-1,-1)

for i in range(r):
    tmp = list(input())
    lake.append(tmp)
    if end != (-1,-1):
        continue
    for j in range(c):
        if tmp[j] == 'L':
            if start == (-1,-1):
                start = [i,j]
            else:
                end = (i,j)

INF = int(1e9)

visited = [[INF]*c for _ in range(r)]
melt_day = [[INF]*c for _ in range(r)]

def melt_lake(graph,melt_day,start):
    queue = deque([start])
    melt_day[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == 'X':
                if melt_day[nx][ny] > melt_day[vx][vy] + 1:
                    melt_day[nx][ny] = melt_day[vx][vy] + 1
                    queue.append((nx,ny))
            else:
                if melt_day[nx][ny] != 0:
                    melt_day[nx][ny] = 0
                    queue.append((nx,ny))


melt_lake(lake,melt_day,start)

def solution(melt_day,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if visited[nx][ny] > max(melt_day[nx][ny],visited[vx][vy]):
                visited[nx][ny] = max(melt_day[nx][ny],visited[vx][vy])
                queue.append((nx,ny))

solution(melt_day,visited,start)

answer = visited[end[0]][end[1]]

print(answer)