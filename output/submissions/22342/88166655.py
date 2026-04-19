n,m = map(int,input().split())

array = [list(input()) for _ in range(n)]

dp = [[0]*(m+2) for _ in range(n+2)]

answer = 0

for y in range(n):
    for x in range(n):
        dp[x][y+1] = max(dp[x+1][y],dp[x][y],dp[x-1][y]) + int(array[x][y])
        answer = max(answer,dp[x][y+1])
        
print(answer)