import sys
input = sys.stdin.readline

n,k = map(int,input().split())

dp = [[0] * (n+1)for _ in range(k+1)]

knapsack = []

for i in range(n):
    w, v = map(int,input().split())
    knapsack.append((w,v))

knapsack.sort()

for i in range(1,n+1):
    for j in range(1,k+1):
        if knapsack[i-1][0] > j:
            dp[j][i] = dp[j][i-1]
        else:
            dp[j][i] = max(dp[j][i-1],dp[j-knapsack[i-1][0]][i-1] + knapsack[i-1][1])


print(dp[k][n])