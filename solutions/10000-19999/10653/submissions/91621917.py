n,k = map(int,input().split())

pos = [list(map(int,input().split())) for _ in range(n)]

INF = int(1e9)

dp = [[INF]*(k+1) for _ in range(n)]

dp[0][0] = 0

for i in range(n):
    x,y = pos[i]
    for j in range(k+1):
        for l in range(k+1):
            if j + l > k or i + l + 1 >= n: break
            nx,ny = pos[i+l+1]
            dp[i+l+1][j+l] = min(dp[i+l+1][j+l],dp[i][j]+abs(nx-x)+abs(ny-y))

print(min(dp[n-1]))