import sys

input = sys.stdin.readline
r,c = map(int,input().split())
graph = []

for _ in range(r):
    graph.append(list(input()))

answer = 0
visited = [[False]*c for _ in range(r)]

def dfs(graph,visited,start):
    x,y = start
    if y == c-1:
        visited[x][y] = True
        return 1
    ny = y + 1
    for dx in range(-1,2):
        nx = x + dx
        if nx < 0 or nx >= r or visited[nx][ny] == True or graph[nx][ny] == 'x':
            continue 
        if dfs(graph,visited,(nx,ny)) == 1:
            visited[x][y] = True
            return 1
    return 0

for i in range(r):
    answer += dfs(graph,visited,(i,0))

print(answer)