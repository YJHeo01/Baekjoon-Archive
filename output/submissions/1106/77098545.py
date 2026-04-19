c,n = map(int,input().split())

marketing = []

max_customer = 0

for _ in range(n):
    cost, customer = map(int,input().split())
    max_customer = max(customer,max_customer)
    marketing.append((cost,customer))

INF = int(1e9)

length = c + max_customer + 1

dp = [INF] * length
dp[0] = 0

for cost, customer in marketing:
    for i in range(customer,length):
        dp[i] = min(dp[i],dp[i-customer]+cost)

answer = min(dp[c:])

print(answer)