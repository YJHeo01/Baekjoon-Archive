import sys

input = sys.stdin.readline

n,k = map(int,input().split())

dp = [0] * (k+1)
dp[0] = 1
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

for coin in coin_list:
    for i in range(coin,k+1):
        dp[i] += dp[i-coin]

print(dp[k])