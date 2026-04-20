n = int(input())

dp = [100001] * (n+1)
dp[0] = 0
l = int(abs(n))

num_list = []

for i in range(1,l+1):
    num_list.append(i*i)

for i in range(1,n+1):
    for j in num_list:
        if i < j:
            continue
        dp[i] = min(dp[i-j]+1,dp[i])

print(dp[n])