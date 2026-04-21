INF = int(1e15)

n = int(input())

array = list(map(int,input().split()))

dp = [[-INF]*(5) for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
    dp[i+1][0] = dp[i][0] + array[i]

for i in range(1,5):
    for j in range(n):
        dp[j+1][i] = max(dp[j][i],dp[j][i-1]) + (1+i%2) * array[j]

print(max(dp[n]))