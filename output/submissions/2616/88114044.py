n = int(input())

array = list(map(int,input().split()))

prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + array[i]

dp = [[0]*n for _ in range(4)]

k = int(input())

for i in range(1,4):
    for j in range(n):
        if j + k >= n: break
        dp[i][j+k] = dp[i-1][j-k]+prefix_sum[j+k]-prefix_sum[j]

print(max(dp[3]))