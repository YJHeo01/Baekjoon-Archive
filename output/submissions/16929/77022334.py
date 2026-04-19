n,m = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(input()))

visited = [[False]*m for _ in range(n)]

cycle = 0

def dfs(graph,visited,last_node,cur_node):
    x,y = cur_node
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or (nx,ny) == last_node:
            continue
        if graph[x][y] == graph[nx][ny]:
            if visited[nx][ny] == True:
                return 1
            visited[nx][ny] = True
            ret_value += dfs(graph,visited,cur_node,(nx,ny))
    return ret_value

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            visited[i][j] = True
            cycle += dfs(board,visited,(i,j),(i,j))

if cycle > 0:
    print("Yes")
else:
    print("No")