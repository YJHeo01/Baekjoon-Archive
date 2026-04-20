from collections import deque

n,m = map(int,input().split())

board = []

for _ in range(n):
    tmp = list(input())
    for i in range(m):
        if tmp[i] == 'H':
            continue
        tmp[i] = int(tmp[i])
    board.append(tmp)

def bfs(graph,visited):
    visited[0][0] = 1
    ret_value = 1
    queue = deque([(0,0)])
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i] * graph[vx][vy]
            ny = vy + dy[i] * graph[vx][vy]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'H':
                continue
            if visited[nx][ny] != 0:
                return -1
            visited[nx][ny] = visited[vx][vy] + 1
            queue.append((nx,ny))
            ret_value = max(ret_value,visited[nx][ny])
    return ret_value

visited = [[0]*m for _ in range(n)]

print(bfs(board,visited))