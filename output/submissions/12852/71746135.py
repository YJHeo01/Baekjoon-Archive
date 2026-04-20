n = int(input())


INF = int(1e9)

dp = [INF] * (n+1)

dp[0] = []

for i in range(1,n+1):
    dp[i] = dp[i-1] + [i]
    if i % 3 == 0:
        if len(dp[i]) > len(dp[i//3]) + 1:
            dp[i] = dp[i//3] + [i]
    if i % 2 == 0:
        if len(dp[i]) > len(dp[i//2]) + 1:
            dp[i] = dp[i//2] + [i]

dp[n].reverse()

print(len(dp[n])-1)

for i in dp[n]:
    print(i,end=" ")