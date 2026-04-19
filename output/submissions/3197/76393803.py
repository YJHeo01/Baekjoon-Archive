from collections import deque
import sys

input = sys.stdin.readline

r,c = map(int,input().split())

lake = []

for _ in range(r):
    lake.append(list(input()))

melt_time = [[0]*c for _ in range(r)]

start = (-1,-1)
end = (-1,-1)

INF = int(1e9)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

bfs_start = []

for x in range(r):
    for y in range(c):
        if lake[x][y] == 'X':
            melt_time[x][y] = INF
        else:
            if lake[x][y] == 'L':
                if start == (-1,-1):
                    start = (x,y)
                else:
                    end = (x,y)
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue
                if lake[nx][ny] == 'X':
                    bfs_start.append((x,y))
                    break
    
def bfs(visited,start):
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
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

bfs(melt_time,bfs_start)

visited = [[INF]*c for _ in range(r)]

def solution(melt_time,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if visited[nx][ny] > max(visited[vx][vy],melt_time[nx][ny]):
                visited[nx][ny] = max(visited[vx][vy],melt_time[nx][ny])
                queue.append((nx,ny))

solution(melt_time,visited,start)

answer = visited[end[0]][end[1]]

print(answer)