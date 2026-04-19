array = [list(map(int,input().split())) for _ in range(5)]

visited = [[0]*5 for _ in range(5)]

r,c = map(int,input().split())

def dfs(array,visited,start):
    x,y = start
    if visited[x][y] == 4: return array[x][y]
    ret_value = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5: continue
        if visited[nx][ny] != 0 or array[nx][ny] == -1: continue
        visited[nx][ny] = visited[x][y] + 1
        ret_value = max(ret_value,dfs(array,visited,(nx,ny)))
        visited[nx][ny] = 0
    ret_value += array[x][y]
    return ret_value

visited[r][c] = 1

cnt = dfs(array,visited,(r,c))

if cnt >= 2:print(1)
else: print(0)