n = int(input())

array = list(map(int,input().split()))

prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + array[i]

dp = [[0]*(n+1) for _ in range(4)]

k = int(input())

for i in range(1,4):
    for j in range(k*i,n+1):
        dp[i][j] = max(dp[i][j-1],dp[i-1][j-k]+prefix_sum[j]-prefix_sum[j-k])

print(max(dp[3]))