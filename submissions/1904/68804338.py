n = int(input())
if n < 4:
    print(n)
else:
    dp = [0] * (n+1)
    dp[1],dp[2],dp[3] = 1,2,3
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        if dp[i] > 15746:
            dp[i] %= 15746
    print(dp[n])