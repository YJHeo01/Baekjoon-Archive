n = int(input())

graph = [[0]*(n+1)]

for _ in range(n):
    graph.append([0] + list(map(int,input().split())))

dp = [[[0]*(n+1) for _ in range(n+1)]for _ in range(3)]

dp[0][1][2] = 1

for i in range(1,n+1):
    for j in range(i,n+1):
        if graph[i][j] == 1:
            dp[0][i][j],dp[1][i][j],dp[2][i][j] = 0,0,0
            continue
        dp[0][i][j] = max(dp[1][i][j-1] + dp[0][i][j-1],dp[0][i][j])
        dp[2][i][j] = max(dp[1][i-1][j] + dp[2][i-1][j],dp[2][i][j])
        if graph[i-1][j] == 0 and graph[i][j-1] == 0:
            dp[1][i][j] = max(dp[1][i][j],dp[0][i-1][j-1]+dp[1][i-1][j-1]+dp[2][i-1][j-1])
        else:
            dp[1][i][j] = 0
    for j in range(i,n+1):
        if graph[j][i] == 1:
            dp[0][j][i],dp[1][j][i],dp[2][j][i] = 0,0,0
            continue
        dp[0][j][i] = max(dp[1][j][i-1] + dp[0][j][i-1],dp[0][j][i])
        dp[2][j][i] = max(dp[1][j-1][i] + dp[2][j-1][i],dp[2][j][i])
        if graph[j-1][i] == 0 and graph[j][i-1] == 0:
            dp[1][j][i] = max(dp[1][j][i],dp[0][j-1][i-1]+dp[1][j-1][i-1]+dp[2][j-1][i-1])
        else:
            dp[1][j][i] = 0

print(dp[0][n][n]+dp[1][n][n]+dp[2][n][n])