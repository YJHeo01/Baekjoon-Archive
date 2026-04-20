from collections import deque

board = []

for _ in range(5):
    board.append(list(input()))

block = []
block_cnt = 0
for i in range(5):
    for j in range(5):
        if board[i][j] == '*':
            block.append((i,j))
            block_cnt += 1

INF = int(1e9)

visited = [[[INF]*block_cnt for _ in range(5)]for _ in range(5)]

def bfs(visited,start,idx):
    queue = deque([])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = start
    visited[x][y][idx] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue
        visited[nx][ny][idx] = 0
        queue.append((nx,ny))
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if visited[nx][ny][idx] > visited[vx][vy][idx] + 1:
                visited[nx][ny][idx] = visited[vx][vy][idx] + 1
                queue.append((nx,ny))

for i in range(block_cnt):
    bfs(visited,block[i],i)

answer = INF

for i in range(5):
    for j in range(5):
        answer = min(answer,sum(visited[i][j][:]))

def check_init_connect(graph,visited,start):
    queue = deque([start])
    visited_cnt = 1
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or graph[nx][ny] == '.':
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                visited_cnt += 1
                queue.append((nx,ny))
        
    if visited_cnt == block_cnt:
        return True
    else:
        return False
original_connect_visited = [[False]*5 for _ in range(5)]

if check_init_connect(board,original_connect_visited,block[0]) == True:
    answer = 0
print(answer)