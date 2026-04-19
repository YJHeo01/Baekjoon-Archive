INF = int(1e15)

n = int(input())

array = list(map(int,input().split()))

dp = [[-INF]*(n+1) for _ in range(5)]

for i in range(5): dp[i][0] = 0

for i in range(n):
    dp[0][i+1] = dp[0][i] + array[i]

for i in range(n):
    dp[1][i+1] = max(dp[0][i],dp[1][i]) + 2 * array[i]

for i in range(n):
    dp[2][i+1] = max(dp[1][i],dp[2][i]) + array[i]

for i in range(n):
    dp[3][i+1] = max(dp[2][i],dp[3][i]) + 2 * array[i]

for i in range(n):
    dp[4][i+1] = max(dp[3][i],dp[4][i]) + array[i]

answer = -INF

for i in range(5):
    answer = max(answer,dp[i][n])

print(answer)