INF = int(1e9)

n,m = map(int,input().split())

byte = list(map(int,input().split()))
cost = list(map(int,input().split()))

dp = [INF]*(m+1)
dp[0] = 0

for i in range(n):
    app_byte = byte[i]; app_cost = cost[i]
    for vx in range(m,app_byte-1,-1):
        dp[vx] = min(dp[vx-app_byte]+app_cost,dp[vx])

print(dp[m])