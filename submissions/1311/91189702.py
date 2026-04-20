n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

INF = int(1e9)

dp = [[INF]*(1<<n) for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
    for j in range(1<<n):
        if dp[i][j] >= INF: continue
        for k in range(n):
            if j & (1<<k) != 0: continue
            dp[i+1][j+(1<<k)] = min(dp[i+1][j+(1<<k)],dp[i][j]+arr[i][k])
            
print(dp[n][(1<<n)-1])