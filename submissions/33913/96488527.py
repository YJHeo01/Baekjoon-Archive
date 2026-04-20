n = int(input())

dp = [[0]*2 for _ in range(n+1)]

dp[1][0] = 24
dp[1][1] = 2

for i in range(2,n+1):
    dp[i][1] += 2 * dp[i-1][0]
    dp[i][0] += 2 * dp[i-1][1]
    for j in range(2):
        dp[i][j] += dp[i-1][j] * 24
        dp[i][j] %= (int(1e9)+7)
        
print(dp[n][0]) 