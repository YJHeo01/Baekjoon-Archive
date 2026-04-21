from collections import deque

INF = int(1e9)

answer = 2001

n, m = map(int,input().split())

def bfs(graph,visited,block_visited):
    queue = deque([(0,0,0)])
    visited[0][0], block_visited[0][0] = 1, 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vx, vy, break_block = queue.popleft()
        if vx == (n-1) and vy == (m-1) and break_block == 1:
            return
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                append = 0
                if break_block == 0 and visited[nx][ny] > visited[vx][vy] + 1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    append = 1
                if visited[nx][ny] > block_visited[vx][vy] + 1:
                    block_visited[nx][ny] = block_visited[vx][vy] + 1
                    append = 1
                if append != 0:
                    queue.append((nx,ny,break_block))
            else:
                if break_block == 0 and visited[nx][ny] > block_visited[vx][vy] + 1:
                    block_visited[nx][ny] = block_visited[vx][vy] + 1
                    queue.append((nx,ny,1))
        



                
        




graph = []

for _ in range(n):
    tmp = list(input())
    for i in range(m):
        tmp[i] = int(tmp[i])
    graph.append(tmp)

visited = [[INF] * m for _ in range(n)]
visited_ = [[INF]*m for _ in range(n)]
bfs(graph,visited,visited_)

answer = min(visited[n-1][m-1],visited_[n-1][m-1])
if answer == INF:
    answer = -1

print(answer)