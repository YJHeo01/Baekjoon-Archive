import sys

input = sys.stdin.readline

n = int(input())
consulting = []

dp = [0] * (n+1)

for _ in range(n):
    time, price = map(int,input().split())
    consulting.append((time,price))

for i in range(n-1,-1,-1):
    dp[i] = dp[i+1]
    if i + consulting[i][0] <= n:
        dp[i] = max(dp[i+consulting[i][0]]+consulting[i][1],dp[i])

print(dp[0])