from collections import deque
import sys


input = sys.stdin.readline

r,c = map(int,input().split())

lake = []


swan1 = (-1,-1)
swan2 = (-1,-1)

for i in range(r):
    tmp = list(input().rstrip())
    lake.append(tmp)
    if swan2 != (-1,-1):
        continue
    for j in range(c):
        if tmp[j] == 'L':
            if swan1 == (-1,-1):
                swan1 = (i,j)
            else:
                swan2 = (i,j)

INF = int(1e9)
visited = [[INF]*c for _ in range(r)]

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
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
                if visited[nx][ny] > visited[vx][vy] + 1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
            else:
                if visited[nx][ny] > visited[vx][vy]:
                    visited[nx][ny] = visited[vx][vy]
                    queue.append((nx,ny))

bfs(lake,visited,swan1)

answer = 0

if visited[swan2[0]][swan2[1]] % 2 == 1:
    answer += 1

answer += (visited[swan2[0]][swan2[1]] // 2)

print(answer)