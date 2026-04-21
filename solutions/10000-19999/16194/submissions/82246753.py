n = int(input())

INF = int(1e9)

dp = [INF] * (n+1)

card = [0] + list(map(int,input().split()))

dp[0] = 0

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = min(dp[i],dp[i-j]+card[j])

print(dp[n])