from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

forest = []

for _ in range(n):
    forest.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 0

def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 1
    ret_value = 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > graph[vx][vy] and visited[vx][vy] + 1 > visited[nx][ny]:
                visited[nx][ny] = visited[vx][vy] + 1
                ret_value = max(ret_value,visited[nx][ny])
                queue.append((nx,ny))
    return ret_value
visited = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        start_searching = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if forest[x][y] >= forest[nx][ny]:
                start_searching = False
                break
        if start_searching == True:
            answer = max(answer,bfs(forest,visited,(x,y)))

print(answer)