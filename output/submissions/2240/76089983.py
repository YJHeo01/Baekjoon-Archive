import sys

input = sys.stdin.readline

t,w = map(int,input().split())

tree = [[0]*3 for _ in range(t+1)]

dp = [[[0]*3 for _ in range(t+1)]for _ in range(w+1)]

for i in range(1,t+1):
    idx = int(input())
    tree[i][idx] = 1
    dp[0][i][1] = dp[0][i-1][1] + tree[i][1]

answer = max(dp[0][t][1],dp[0][t][2])

for i in range(1,w+1):
    for j in range(1,t+1):
        dp[i][j][1] = max(dp[i-1][j-1][2],dp[i][j-1][1]) + tree[j][1]
        dp[i][j][2] = max(dp[i-1][j-1][1],dp[i][j-1][2]) + tree[j][2]
    answer = max(answer,dp[i][t][1],dp[i][t][2])

print(answer)