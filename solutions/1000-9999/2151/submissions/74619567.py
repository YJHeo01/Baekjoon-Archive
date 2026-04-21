from collections import deque

n = int(input())

house = []

mirror = []

for i in range(n):
    tmp = list(input())
    house.append(tmp)
    for j in range(n):
        if tmp[j] == '#':
            mirror.append([i,j])

INF = int(1e9)

visited = [[[INF]*n for _ in range(n)]for _ in range(4)]

def bfs(graph,visited,start):
    queue = deque([])
    for i in range(4):
        visited[i][start[0]][start[1]] = 0
        queue.append(start+[i])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while queue:
        vx,vy,d = queue.popleft()
        nx = vx + dx[d]
        ny = vy + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == '*':
            continue
        if visited[d][nx][ny] > visited[d][vx][vy]:
            visited[d][nx][ny] = visited[d][vx][vy]
            queue.append((nx,ny,d))
        if graph[nx][ny] == '!':
            for i in [1,-1]:
                nd = (d + i) % 4
                if visited[nd][nx][ny] > visited[d][nx][ny] + 1:
                    visited[nd][nx][ny] = visited[d][nx][ny] + 1
                    queue.append((nx,ny,nd))

bfs(house,visited,mirror[0])

answer = INF

for i in range(4):
    answer = min(answer,visited[i][mirror[1][0]][mirror[1][1]])

print(answer)