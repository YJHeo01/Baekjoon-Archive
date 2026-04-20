m,n= map(int,input().split())

ground = []

for _ in range(m):
    ground.append(list(map(int,input().split())))

def dfs(x,y):
    if x == (m-1) and y == (n-1):
        return 1
    ret_value = 0
    if x - 1 >= 0 and ground[x][y] > ground[x-1][y]:
        ret_value += dfs(x-1,y)
    if y - 1 >= 0 and ground[x][y] > ground[x][y-1]:
        ret_value += dfs(x,y-1)
    if x + 1 < m and ground[x][y] > ground[x+1][y]:
        ret_value += dfs(x+1,y)
    if y + 1 < n and ground[x][y] > ground[x][y+1]:
        ret_value += dfs(x,y+1)
    return ret_value

print(dfs(0,0))