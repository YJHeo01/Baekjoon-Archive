import sys

input = sys.stdin.readline

graph = []

m,n = map(int,input().split())

for _ in range(m):
    graph.append(list(map(int,input().split())))

def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1 
    ret_value = 0
    if x - 1 >= 0 and graph[y][x] > graph[y][x-1]:
        ret_value += dfs(x-1,y)
    if y - 1 >= 0 and graph[y][x] > graph[y-1][x]:
        ret_value += dfs(x,y-1)
    if x + 1 < n and graph[y][x] > graph[y][x+1]:
        ret_value += dfs(x+1,y)
    if y + 1 < m and graph[y][x] > graph[y+1][x]:
        ret_value += dfs(x,y+1)
    return ret_value
    
print(dfs(0,0))