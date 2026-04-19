n = int(input())

stone = [list(map(int,input().split())) for _ in range(n-1)]

stone.append([0,0])

k = int(input())

dp = [[int(1e9)]*2 for _ in range(n+1)]

dp[0][0] = 0

for i in range(n-1):
    for j in [1,2]:
        dp[i+j][0] = min(dp[i+j][0],dp[i][0]+stone[i][0])
        dp[i+j][1] = min(dp[i+j][1],dp[i][1]+stone[i][1])
    if i != n-2:
        dp[i+3][1] = min(dp[i+3][1],dp[i][0]+k)

answer = min(min(dp[n-1]),min(dp[n]))
    
print(answer)