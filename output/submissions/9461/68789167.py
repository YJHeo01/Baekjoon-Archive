t = int(input())
dp = [0,1,1,1,2,2,3,4]
for i in range(t):
    n = int(input())
    if n <= 7:
        print(dp[n])
    else:
        new_dp = [0] * (n+1)
        for i in range(8):
            new_dp[i] = dp[i]
        for i in range(8,n+1):
            new_dp[i] = new_dp[i-1] + new_dp[i-5]
        print(new_dp[i])