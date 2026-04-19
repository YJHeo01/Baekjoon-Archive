n = int(input())
array = list(map(int,input().split()))

INF = int(1e9)

answer = max(array[0],array[1])


dp = [[-INF]*n for _ in range(2)]
dp[0][0] = array[0]
dp[1][0] = array[0]
dp[1][1] = array[1]
for i in range(1,n):
    dp[0][i] = max(dp[0][i-1],0) + array[i]
    answer = max(answer,dp[0][i])

for i in range(2,n):
    dp[1][i] = max(dp[1][i-1],dp[0][i-2]) + array[i]
    answer = max(answer,dp[1][i])

print(answer)