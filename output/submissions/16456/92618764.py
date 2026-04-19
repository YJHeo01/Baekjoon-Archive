INF = 1000000009

n = int(input())

dp = [0] * (n+1)

dp[0] = 1

for i in range(n):
    dp[i] %= INF
    dp[i+1] += dp[i]
    if i + 3 <= n: dp[i+3] += dp[i]

dp[n] %= INF

print(dp[n])