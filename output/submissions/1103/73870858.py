n,m = map(int,input().split())

board = []

for _ in range(n):
    tmp = list(input())
    for i in range(m):
        if tmp[i] == 'H':
            continue
        tmp[i] = int(tmp[i])
    board.append(tmp)
INF= int(1e9)

def dfs(graph,visited,start):
    x,y = start
    dx = [graph[x][y],-graph[x][y],0,0]
    dy = [0,0,graph[x][y],-graph[x][y]]
    ret_value = visited[x][y]
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
answer = dfs(board,visited,(0,0)) + 1
if answer >= INF:
    answer = -1
print(answer)