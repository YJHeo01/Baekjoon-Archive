n,m,t = map(int,input().split())

work = [list(map(int,input().split())) for _ in range(n)]

time = [list(map(int,input().split())) for _ in range(n)]

dp = [[[-int(1e9)]*(t+1) for _ in range(m)] for _ in range(n)]

dp[0][0][t] = 0

for x in range(n):
    for y in range(m):
        for k in range(time[x][y],t+1):
            dp[x][y][k-time[x][y]] = max(dp[x][y][k-time[x][y]],dp[x][y][k]+work[x][y])
        for k in range(t,0,-1):
            for dx,dy in [(0,1),(1,0),(1,1)]:
                nx = x + dx
                ny = y + dy
                if nx >= n or ny >= m: continue
                dp[nx][ny][k-1] = max(dp[nx][ny][k-1],dp[x][y][k])

answer = max(dp[n-1][m-1])

print(answer)