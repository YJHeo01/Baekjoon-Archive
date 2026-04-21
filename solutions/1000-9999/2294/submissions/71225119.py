#https://github.com/YJHeo01

n,k = map(int,input().split())

coin_list = []

for _ in range(n):
    coin_list.append(int(input()))

INF = int(1e9)
dp = [INF] * (k+1)
dp[0] = 0

for coin in coin_list:
    for i in range(coin,k+1):
        if dp[i] > dp[i-coin] + 1:
            dp[i] = dp[i-coin] + 1

print(dp[k])