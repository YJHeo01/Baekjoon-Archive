m,n= map(int,input().split())

ground = []

INF = 10001
ground.append([INF]*(m+2))

for _ in range(m):
    ground.append([INF] + list(map(int,input().split())) + [INF])

ground.append([INF]*(m+2))

def dfs(x,y):
    if x == m and y == n:
        return 1
    ret_value = 0
    if ground[x][y] > ground[x-1][y]:
        ret_value += dfs(x-1,y)
    if ground[x][y] > ground[x][y-1]:
        ret_value += dfs(x,y-1)
    if ground[x][y] > ground[x+1][y]:
        ret_value += dfs(x+1,y)
    if ground[x][y] > ground[x][y+1]:
        ret_value += dfs(x,y+1)
    return ret_value

print(dfs(1,1))