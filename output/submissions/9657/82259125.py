INF = 1001

n = int(input())

dp = [0] * INF
dp[0] = 2

for i in range(1001):
    for dx in [1,3,4]:
        if i + dx < INF and dp[i+dx] == 0:
            if dp[i] == 1:
                dp[i+dx] = 2
            elif dp[i] == 2:
                dp[i+dx] = 1
            else:
                dp[i+dx] = dp[i]

if dp[n] == 1:
    print("SK")
else:
    print("CY")