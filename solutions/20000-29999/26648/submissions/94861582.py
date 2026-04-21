n = int(input())

arr = [list(map(int,input().split())) for _ in range(3)]

INF = int(1e10)

dp = [[INF]*2 for _ in range(n+1)]

dp[0][0] = -1

for i in range(n):
    tmp = sorted([arr[0][i],arr[1][i],arr[2][i]])
    if tmp[1] > dp[i][0]: 
        dp[i+1][0] = tmp[1]
    if tmp[1] > dp[i][1]:
        dp[i+1][1] = tmp[1]
    if i != 0 and tmp[2] <= dp[i][1]:
        print("NO")
        exit(0)
    if i != 0:
        dp[i+1][1] = min(dp[i][0] + 1,dp[i+1][1])
    else:
        dp[i+1][1] = tmp[0]

print("YES")