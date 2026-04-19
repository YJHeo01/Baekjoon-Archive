from collections import deque
import sys

input = sys.stdin.readline

w,h = map(int,input().split())

graph = []

start, end = (-1,-1), (-1,-1)

for i in range(h):
    tmp = list(input())
    graph.append(tmp)
    for j in range(w):
        if tmp[j] == 'C':
            if start == (-1,-1):
                start = (i,j)
            else:
                end = (i,j)

INF = int(1e9)
visited = [[[INF]*4 for _ in range(w)]for _ in range(h)]

def solution(graph,visited,start):
    start_x, start_y = start
    queue = deque([])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        visited[start[0]][start[1]][i] = 0
        queue.append((start_x,start_y,i))
    while queue:
        vx,vy,d = queue.popleft()
        nx = vx + dx[d]
        ny = vy + dy[d]
        if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '*':
            continue
        if visited[nx][ny][d] > visited[vx][vy][d]:
            visited[nx][ny][d] = visited[vx][vy][d]
            queue.append((nx,ny,d))
        for i in [-1,1]:
            nd = (d+i) % 4
            if visited[nx][ny][nd] > visited[nx][ny][d] + 1:
                visited[nx][ny][nd] = visited[nx][ny][d] + 1
                queue.append((nx,ny,nd))
end_x, end_y = end
solution(graph,visited,start)
answer = min(visited[end_x][end_y][:])
print(answer)