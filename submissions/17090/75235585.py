import sys

input = sys.stdin.readline

n,m = map(int,input().split())

ground = []

for _ in range(n):
    ground.append(list(input()))

visited = [[False]*m for _ in range(n)]
escape_zone = [[False]*m for _ in range(n)]
move_type = {'U':0,'D':1,'L':2,'R':3}

def dfs(graph,visited,position,escape_zone):
    x,y = position
    if x < 0 or y < 0 or x >= n or y >= m or escape_zone[x][y] == True:
        return 0
    if visited[x][y] == True:
        return -1
    visited[x][y] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    i = move_type[graph[x][y]]
    nx, ny = x + dx[i], y + dy[i]
    ret_value = dfs(graph,visited,(nx,ny),escape_zone)
    if ret_value >= 0:
        escape_zone[x][y] = True
        ret_value += 1
    return ret_value


answer = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            tmp = dfs(ground,visited,(i,j),escape_zone)
            if tmp > 0:
                answer += tmp

print(answer)