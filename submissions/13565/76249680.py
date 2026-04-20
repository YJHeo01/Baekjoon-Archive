from collections import deque

m,n = map(int,input().split())

board = []

for _ in range(m):
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
            if nx < 0 or ny < 0 or nx >= m or ny >= n or visited[nx][ny] == True:
                continue
            if graph[nx][ny] == '0':
                visited[nx][ny] = True
                queue.append((nx,ny))
    
visited = [[False]*n for _ in range(m)]

for i in range(n):
    if board[0][i] == '0' and visited[0][i] == False:
        bfs(board,visited,(0,i))

no = True

for i in range(n):
    if visited[m-1][i] == True:
        no = False
        break

if no == True:
    print("NO")
else:
    print("YES")