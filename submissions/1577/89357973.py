n,m = map(int,input().split())

k = int(input())

block = [[[False]*2 for _ in range(m+1)] for _ in range(n+1)]

dx = [1,0]
dy = [0,1]

for _ in range(k):
    a,b,c,d = map(int,input().split())
    if a > c: a,c = c,a
    if b > d: b,d = d,b
    if c > a:
        block[a][b][0] = True
    else:
        block[a][b][1] = True

dp = [[0]*(m+1) for _ in range(n+1)]

dp[0][0] = 1

for nx in range(n+1):
    for ny in range(m+1):
        for i in range(2):
            vx = nx - dx[i]
            vy = ny - dy[i]
            if vx < 0 or vy < 0 or block[vx][vy][i]: continue
            dp[nx][ny] += dp[vx][vy]

print(dp[n][m])