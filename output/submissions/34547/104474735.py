n = int(input())

a0,b0,k = map(int,input().split())

INF = int(1e9)

dp = [[-INF]*(a0+b0+1) for _ in range(n+1)]

dp[0][a0] = 0

for day in range(n):
    for a in range(a0+b0+1):
        if dp[day][a] <= -INF: continue
        b = a0 + b0 - a
        for plus in range(k,b+1):
            next_a = a + plus
            next_b = b - plus
            dp[day+1][next_a] = max(dp[day+1][next_a],dp[day][a]+next_a*next_b)
        for minus in range(k,a+1):
            next_a = a - minus
            next_b = b + minus
            dp[day+1][next_a] = max(dp[day+1][next_a],dp[day][a]+next_a*next_b)

print(max(dp[n]))