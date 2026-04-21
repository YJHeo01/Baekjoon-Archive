from collections import deque

n = int(input())


def bfs(graph,visited,start):
    queue = deque([start])
    dx = [[0,1],[1,1],[0,1,1]]
    dy = [[1,1],[0,1],[1,1,0]]
    while queue:
        vx, vy, d = queue.popleft()
        l = len(dx[d])
        for i in range(l):
            nx = vx + dx[d][i]
            ny = vy + dy[d][i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if i == 1:
                if graph[nx][ny] == 1 or graph[nx][ny-1] == 1 or graph[nx-1][ny] == 1:
                    continue
                visited[nx][ny] += 1
                queue.append((nx,ny,2))
            else:
                if graph[nx][ny] == 1:
                    continue
                visited[nx][ny] += 1
                if dx[d][i] == 1:
                    queue.append((nx,ny,1))
                else:
                    queue.append((nx,ny,0))