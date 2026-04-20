INF = int(1e9)

n,m = map(int,input().split())

byte = list(map(int,input().split()))
cost = list(map(int,input().split()))

dp = [INF]* (sum(byte) + 1)
dp[0] = 0
length = 0

for i in range(n):
    app_byte = byte[i]; app_cost = cost[i]
    length += app_byte
    length = min(length,m+app_byte)
    for vx in range(length,app_byte-1,-1):
        dp[vx] = min(dp[vx-app_byte]+app_cost,dp[vx])

answer = min(dp[m:])

print(answer)