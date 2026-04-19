INF = 2501

n,m = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(m):
        if board[i][j] != 'H':
            board[i][j] = int(board[i][j])

def dfs(graph,visited,start):
    vx, vy = start
    ret_value = visited[vx][vy]
    move_size = graph[start[0]][start[1]]
    dx = [move_size,0,-move_size,0]
    dy = [0,move_size,0,-move_size]
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 'H':
            continue
        if visited[nx][ny] == 0:
            visited[nx][ny] = visited[vx][vy] + 1
            ret_value = max(dfs(graph,visited,(nx,ny)),ret_value)
        elif visited[nx][ny] < visited[vx][vy]:
            ret_value = INF
            visited[vx][vy] = INF
            return INF
    visited[vx][vy] = ret_value
    return ret_value

visited = [[0]*m for _ in range(n)]

answer = dfs(board,visited,(0,0))

if answer >= INF:
    answer = -1
else:
    answer += 1
print(answer)