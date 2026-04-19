c,n = map(int,input().split())

city = []

for _ in range(n):
    cost,customer = map(int,input().split())
    city.append((customer,cost))

city.sort()

INF = int(1e9)

dp = [INF] * (c+1)
dp[0] = 0

for customer,cost in city:
    for i in range(customer,c+1):
        dp[i] = min(dp[i],dp[i-customer]+cost)
    start = (c//customer) * customer
    for i in range(start,c):
        dp[c] = min(dp[c],dp[i]+cost)
print(dp[c])