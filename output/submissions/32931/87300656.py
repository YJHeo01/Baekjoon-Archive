n = int(input())
array = [list(map(int,input().split())) for _ in range(2)]
INF = int(1e18)
dp = [[-INF]*(n+1) for _ in range(2)]
dp[1][0] = array[0][0]
dp[1][1] = array[1][0] + dp[1][0]

for i in range(1,n):
    dp[0][i+1] = dp[0][i]
    dp[1][i+1] = dp[1][i]
    dp[0][i+1] += array[0][i]
    dp[1][i+1] += array[1][i]
    if array[1][i] > 0: dp[0][i+1] += array[1][i]
    if array[0][i] > 0: dp[1][i+1] += array[0][i]

print(max(dp[1][n],dp[0][n]+array[1][n-1]))