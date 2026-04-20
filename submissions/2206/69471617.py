from collections import deque

INF = int(1e9)

answer = INF

n, m = map(int,input().split())

def bfs(graph,visited):
    global answer
    queue = deque([(0,0,0)])
    block_queue = deque([])
    visited[0][0] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vx, vy, break_block = queue.popleft()
        if break_block == 1:
            distance = block_queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if nx == (n-1) and ny == (m-1):
                if break_block == 1:
                    answer = distance + 1
                else:
                    answer = visited[vx][vy] + 1
                return
            if break_block == 0:
                if visited[nx][ny] > visited[vx][vy] + 1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny,graph[nx][ny]))
                    if graph[nx][ny] == 1:
                        block_queue.append(visited[nx][ny])
            else:
                if graph[nx][ny] == 0 and visited[nx][ny] > distance + 1:
                    queue.append((nx,ny,1))
                    block_queue.append(distance+1)
        



                
        




graph = []

for _ in range(n):
    tmp = list(input())
    for i in range(m):
        tmp[i] = int(tmp[i])
    graph.append(tmp)

visited = [[INF] * m for _ in range(n)]
bfs(graph,visited)

if answer == INF:
    answer = -1

print(answer)