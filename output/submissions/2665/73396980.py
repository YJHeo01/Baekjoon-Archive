from collections import deque

n = int(input())

array = []

for _ in range(n):
    array.append(list(input()))
INF = int(1e9)

visited = [[INF]*n for _ in range(n)]

def solution(graph,visited):
    queue = deque([(0,0)])
    visited[0][0] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == '1':
                if visited[nx][ny] > visited[vx][vy]:
                    visited[nx][ny] = visited[vx][vy]
                    queue.append((nx,ny))
            else:
                if visited[nx][ny] > visited[vx][vy] + 1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
    return visited[n-1][n-1]

answer = solution(array,visited)

print(answer)