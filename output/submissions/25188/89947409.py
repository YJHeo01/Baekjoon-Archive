INF = int(1e15)

n = int(input())

array = list(map(int,input().split()))

dp = [[-INF]*7 for _ in range(n+1)]

for i in range(7):
    dp[0][i] = 0

for i in range(n):
    for j in range(6):
        if j % 2 == 0:
            dp[i+1][j+1] = max(dp[i][j],dp[i][j+1]) + array[i]
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

print(dp[n][6])