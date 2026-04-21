n = int(input())

arr = [list(map(int,input().split())) for _ in range(3)]

INF = int(1e10)

dp = [[INF]*2 for _ in range(n+1)]

dp[0][0] = -1
dp[0][1] = -1

for i in range(n):
    tmp = sorted([arr[0][i],arr[1][i],arr[2][i]])
    for j in range(2):
        if tmp[1] > dp[i][j]:
            dp[i+1][j] = tmp[1]
    if tmp[0] > dp[i][0]:
        dp[i+1][1] = min(dp[i][1],tmp[0])

if min(dp[n]) == INF:
    print("NO")
else:
    print("YES")