INF = int(1e9)

n,m = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(input()))

def dfs(graph,visited,start):
    x, y = start
    ret_value = visited[x][y]
    move_size = int(graph[x][y])
    dx = [move_size,-move_size,0,0]
    dy = [0,0,move_size,-move_size]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 'H':
            continue
        if visited[nx][ny] != 0:
            return INF
        visited[nx][ny] = visited[x][y] + 1
        ret_value = max(ret_value,dfs(graph,visited,(nx,ny)))
        visited[nx][ny] = 0
    return ret_value

visited = [[0]*m for _ in range(n)]

visited[0][0] = 1
answer = dfs(board,visited,(0,0))
if answer >= INF:
    answer = -1
print(answer)