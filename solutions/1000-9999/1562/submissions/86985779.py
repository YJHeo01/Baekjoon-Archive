INF = 1000000000

n = int(input())

dp = [[[0]*4 for _ in range(10)] for _ in range(n)]

for i in range(1,9):
    dp[0][i][0] = 1

dp[0][9][2] = 1

for length in range(1,n):
    for j in range(4):
        dp[length][0][j|1] += dp[length-1][1][j]
    for i in range(1,9):
        for j in range(4):
            dp[length][i][j] = dp[length-1][i-1][j] + dp[length-1][i+1][j]
    for j in range(4):
        dp[length][9][j|2] += dp[length-1][8][j]

answer = 0

for i in range(10):
    answer += dp[n-1][i][3]
    answer %= INF

print(answer)