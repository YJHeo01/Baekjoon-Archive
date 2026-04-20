#https://github.com/YJHeo01
#https://www.acmicpc.net/problem/2133

n = int(input())

dp = [0] * (n+1)

if n == 1:
    print(0)

else:
    dp[2] = 3

    for i in range(4,n+1):
        dp[i] = dp[i-2] * 2 + 2

    print(dp[n])