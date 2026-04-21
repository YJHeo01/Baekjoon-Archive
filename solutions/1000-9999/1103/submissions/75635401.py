INF = 2501

n,m = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(input()))

def dfs(graph,visited,start):
    ret_value = 0
    vx, vy = start
    visited[vx][vy] = True
    move_size = int(graph[start[0]][start[1]])
    dx = [move_size,0,-move_size,0]
    dy = [0,move_size,0,-move_size]
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 'H':
            continue
        if visited[nx][ny] == True:
            return INF
        ret_value = max(dfs(graph,visited,(nx,ny)),ret_value)
    visited[vx][vy] = False
    ret_value += 1
    return ret_value

visited = [[False]*m for _ in range(n)]

answer = dfs(board,visited,(0,0))

if answer >= INF:
    answer = -1
    
print(answer)