INF = int(1e9)

n,m = map(int,input().split())

byte = list(map(int,input().split()))
cost = list(map(int,input().split()))

dp = [[INF]*(m+1)]
dp[0][0] = 0

for _ in range(n):
    dp.append([INF]*(m+1))

for i in range(1,n+1):
    app_byte = byte[i-1]; app_cost = cost[i-1]
    for vx in range(m+1):
        dp[i][vx] = min(dp[i-1][vx],dp[i][vx])
        nx = min(m,vx + app_byte)
        dp[i][nx] = min(dp[i-1][vx] + app_cost,dp[i][nx])

print(dp[n][m])