s = int(input())

INF = 2 * s
dp = [INF] * (s+1)
dp[1] = 0
for i in range(1,s+1):
    length = s // i
    if dp[i-1] > dp[i] + 1:
        dp[i-1] = dp[i] + 1
    for j in range(2,length+1):
        if dp[i*j] > dp[i] + j:
            dp[i*j] = dp[i] + j

print(dp[s])