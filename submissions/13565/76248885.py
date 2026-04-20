from collections import deque

n,m = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(input()))

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == '0' and visited[nx][ny] == False:
                visited[nx][ny] == True
                queue.append((nx,ny))
    
visited = [[False]*m for _ in range(n)]

for i in range(m):
    if board[0][i] == '0' and visited[0][i] == False:
        bfs(board,visited,(0,i))

no = True

for i in range(m):
    if visited[n-1][i] == True:
        no = False
        break

if no == True:
    print("NO")
else:
    print("YES")