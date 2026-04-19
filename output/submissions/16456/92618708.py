INF = 1000000009

n = int(input())

dp = [0] * (n+1)

dp[0] = 1

answer = 0

for i in range(n):
    dp[i] %= INF
    dp[i+1] += dp[i]
    if i + 3 > n:
        answer += dp[i]
    else:
        dp[i+3] += dp[i]
        
answer += dp[n]

answer %= INF

print(answer)