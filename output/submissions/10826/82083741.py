n = int(input())

if n == 0:
    print(0)
    exit(0)

if n <= 2:
    print(1)
    exit(0)

dp = [0] * (n+1)

for i in range(1,3):
    dp[i] = 1

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])