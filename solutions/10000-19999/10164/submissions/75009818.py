n,m,k = map(int,input().split())

O_x = (k-1)//m + 1
O_y = (k-1)%m + 1

if k == 0:
    O_x, O_y = 1,1
dp = [[0]*(m+1) for _ in range(n+1)]

dp[0][1] = 1

for i in range(1,O_x+1):
    for j in range(1,O_y+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

O_path_cnt = dp[O_x][O_y]

dp = [[0]*(m+1) for _ in range(n+1)]

dp[O_x][O_y] = O_path_cnt


for i in range(O_x,n+1):
    for j in range(O_y,m+1):
        if i == O_x and j == O_y:
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]


print(dp[n][m])
