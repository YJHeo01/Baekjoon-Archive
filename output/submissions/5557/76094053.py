n = int(input())

array = list(map(int,input().split()))
dp = [[0]*21 for _ in range(n-1)]
dp[0][array[0]] = 1

for i in range(1,n-1):
    for vx in range(21):
        if dp[i-1][vx] == 0:
            continue
        nx = vx + array[i]
        if nx <= 20:
            dp[i][nx] += dp[i-1][vx]
        nx = vx - array[i]
        if nx >= 0:
            dp[i][nx] += dp[i-1][vx]

print(dp[n-2][array[-1]])