import sys

input = sys.stdin.readline

n,m = map(int,input().split())

can_escape = [[False]*m for _ in range(n)]
cant_escape = [[False]*m for _ in range(n)]

answer = 0

ground = []

for _ in range(n):
    ground.append(list(input()))

def dfs(graph,can_escape,cant_escape,visited,position):
    x,y = position
    if x < 0 or y < 0 or x >= n or y >= m:
        return 1
    elif visited[x][y] == True:
        cant_escape[x][y] = True
        return 0
    else:
        visited[x][y] = True
        ret_value = 0
        if graph[x][y] == 'D':
            ret_value = dfs(graph,can_escape,cant_escape,visited,(x+1,y))
        elif graph[x][y] == 'U':
            ret_value = dfs(graph,can_escape,cant_escape,visited,(x-1,y))
        elif graph[x][y] == 'L':
            ret_value = dfs(graph,can_escape,cant_escape,visited,(x,y-1))
        else:
            ret_value = dfs(graph,can_escape,cant_escape,visited,(x,y+1))
        if ret_value == 1:
            can_escape[x][y] = True
        else:
            cant_escape[x][y] = True
        return ret_value
    
for i in range(n):
    for j in range(m):
        if can_escape[i][j] == True:
            answer += 1
        elif cant_escape[i][j] == True:
            continue
        else:
            visited = [[False]*m for _ in range(n)]
            answer += dfs(ground,can_escape,cant_escape,visited,(i,j))

print(answer)