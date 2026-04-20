n = int(input())

w = list(map(int,input().split()))

m = int(input())

l = list(map(int,input().split()))

k = int(input())

INF = int(1e9)

dp = [[-INF]*(m+1) for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
    dp[i+1][0] = dp[i][0] + w[i]

for i in range(m):
    dp[0][i+1] = dp[0][i] - l[i]
    if dp[0][i] % k != 0:
        dp[0][i+1] = max(dp[0][i+1],dp[0][i]-min(dp[0][i]%k,l[i]))

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + w[i-1]
        if dp[i][j-1] % k == 0:
            dp[i][j] = max(dp[i][j],dp[i][j-1]-l[j-1])
        else:
            dp[i][j] = max(dp[i][j],dp[i][j-1]-min(l[j-1],dp[i][j-1]%k))
            
print(dp[n][m])