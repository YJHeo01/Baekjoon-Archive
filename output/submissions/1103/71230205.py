#https://github.com/YJHeo01

n,m = map(int,input().split())

board = []

for _ in range(n):
    tmp = list(input())
    for i in range(m):
        if tmp[i] == 'H':
            continue
        tmp[i] = int(tmp[i])
    board.append(tmp)
INF = int(1e9)

def dfs(graph,visited,start):
    ret_value = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = start[0] + dx[i] * graph[start[0]][start[1]]
        ny = start[1] + dy[i] * graph[start[0]][start[1]]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 'H':
            continue
        if visited[nx][ny] != 0:
            return INF
        visited[nx][ny] = visited[start[0]][start[1]] + 1
        ret_value = max(ret_value,dfs(graph,visited,(nx,ny)))
    return max(ret_value,visited[start[0]][start[1]])

visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
answer = dfs(board,visited,(0,0))
if answer == INF:
    answer = -1
print(answer)