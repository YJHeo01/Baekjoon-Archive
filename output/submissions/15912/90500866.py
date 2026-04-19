n = int(input())

W = list(map(int,input().split()))

E = list(map(int,input().split()))

W_max = [[0]*n for _ in range(n)]

E_max = [[0]*n for _ in range(n)]

for i in range(n):
    W_max[i][i] = W[i]
    E_max[i][i] = E[i]
    for j in range(i+1,n):
        W_max[i][j] = max(W_max[i][j-1],W[j])
        E_max[i][j] = max(E_max[i][j-1],E[j])


INF = int(1e9)

dp = [INF] * (n+1)

dp[0] = 0

for i in range(1,n+1):
    dp[i] = dp[i-1] + W[i-1] * E[i-1]
    for j in range(1,i):
        dp[i] = min(dp[i],dp[j-1]+W_max[j-1][i-1]*E_max[j-1][i-1])

print(dp[n])