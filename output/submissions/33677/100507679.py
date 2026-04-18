import math

n = int(input())

INF = int(1e9)

dp = [INF] * (n+1)

dp[0] = 0

qqq = [False] * (n+1)

tmp = 1

while True:
    if tmp * tmp > n: break
    qqq[tmp*tmp] = True
    tmp += 1

water = [INF] * (n+1)
water[0] = 0
for i in range(1,n+1):
    dp[i] = dp[i-1] + 1
    water[i] = water[i-1] + 1
    if i % 3 == 0 and dp[i//3] +1 <= dp[i]:
        dp[i] = dp[i//3]+1
        water[i] = water[i//3] + 3
    if qqq[i] and dp[int(math.sqrt(i))] + 1 < dp[i]:
        dp[i] = dp[int(math.sqrt(i))]+1
        water[i] = water[int(math.sqrt(i))] + 5
    if qqq[i] and dp[int(math.sqrt(i))] + 1 == dp[i]:
        water[i] = min(water[int(math.sqrt(i))] + 5,water[i])

print(dp[n], water[n])