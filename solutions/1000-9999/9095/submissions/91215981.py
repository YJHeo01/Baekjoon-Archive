dp = [0] * 12

dp[0] = 1

for i in range(1,12):
    for j in range(1,4):
        if i - j < 0: continue
        dp[i] += dp[i-j]

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])