n = int(input())

stone = [list(map(int,input().split())) for _ in range(n-1)]

stone.append([0,0])

k = int(input())

dp = [[int(1e9)]*2 for _ in range(n+1)]

dp[0][0] = 0

for i in range(1,n):
    dp[i][0] = dp[i-1][0] + stone[i-1][0]
    dp[i][1] = dp[i-1][1] + stone[i-1][0]
    if i >= 2:
        dp[i][0] = min(dp[i][0],dp[i-2][0]+stone[i-2][1])
        dp[i][1] = min(dp[i][1],dp[i-2][1]+stone[i-2][1])
    if i >= 3:
        dp[i][1] = min(dp[i][1],dp[i-3][0]+k)

answer = min(min(dp[n-1]),min(dp[n]))
    
print(answer)