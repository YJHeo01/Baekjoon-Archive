n = int(input())

P_i = [0] + list(map(int,input().split()))

dp = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i < j:
            continue
        dp[i] = max(dp[i],dp[i-j]+P_i[j])

print(dp[n])