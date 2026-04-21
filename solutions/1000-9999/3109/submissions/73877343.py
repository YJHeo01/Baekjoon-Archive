import sys

input = sys.stdin.readline

r,c = map(int,input().split())

graph = []

for _ in range(r):
    graph.append(list(input()))

def dfs(graph,visited,vx,vy):
    visited[vx][vy] = True
    if vy == r-1:
        return True
    dx = [-1,0,1]
    ny = vy + 1
    for i in range(3):
        nx = vx+ dx[i]
        if nx < 0 or nx >= r or graph[nx][ny] == 'x' or visited[nx][ny] == True:
            continue
        if dfs(graph,visited,nx,ny) == True:
            return True
    visited[vx][vy] = False
    return False

visited = [[False]*c for _ in range(r)]
answer = 0
for i in range(r):
    if dfs(graph,visited,i,0) == True:
        answer += 1

print(answer)
