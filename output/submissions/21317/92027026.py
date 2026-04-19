n = int(input())

stone = [list(map(int,input().split())) for _ in range(n-1)]

stone.append([0,0])

k = int(input())

dp = [int(1e9)] * (n+1)

dp[0] = 0

for i in range(n-1):
    dp[i+1] = min(dp[i+1],dp[i]+stone[i][0])
    dp[i+2] = min(dp[i+2],dp[i]+stone[i][1])

for i in range(n,2,-1):
    dp[i] = min(dp[i],dp[i-3]+k)
    
for i in range(n-1):
    dp[i+1] = min(dp[i+1],dp[i]+stone[i][0])
    dp[i+2] = min(dp[i+2],dp[i]+stone[i][1])
    
print(min(dp[n],dp[n-1]))