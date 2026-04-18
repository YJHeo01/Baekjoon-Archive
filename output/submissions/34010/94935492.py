n = int(input())

graph = [[[]for _ in range(n)] for _ in range(n)]

for i in range(n):
    roads = list(map(int,input().split()))
    for j in range(n-1):
        dist = roads[j]
        graph[i][j].append((i,j+1,dist))
        graph[i][j+1].append((i,j,dist))
    if i == n-1: continue
    roads = list(map(int,input().split()))
    for j in range(n):
        graph[i][j].append((i+1,j,dist))
        graph[i+1][j].append((i,j,dist))


dp = [[[-1]*2 for _ in range(n)] for _ in range(n)]

dx = [0,1]
dy = [1,0]

for x in range(n):
    for y in range(n):
        for i in range(2):
            for k in range(2):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx == n or ny == n: continue
                if i == k:
                    dp[nx][ny][k] == max(dp[x][y][i],dp[nx][ny][k])
                else:
                    dp[nx][ny][k] = max(dp[nx][ny][k],dp[x][y][i]+1)

print(2*(n-1),max(dp[n-1][n-1]))