n = int(input())

dp = [[0]*10 for _ in range(n)]

for i in range(1,10):
    dp[0][i] = 1

dx = [-1,1]
for i in range(n-1):
    for j in range(10):
        for k in range(2):
            nx = j + dx[k]
            if nx < 0 or nx >= 10:
                continue
            dp[i+1][nx] = (dp[i+1][nx] + dp[i][j]) % 1000000000

answer = sum(dp[n-1]) % 1000000000

print(answer)