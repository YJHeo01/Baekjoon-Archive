INF = int(1e18)

import sys

input = sys.stdin.readline

n = int(input())

contest = []

for _ in range(n):
    contest.append(list(map(int,input().split())))

dp = [[INF]*2 for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
    x,p = contest[i]
    if dp[i][0] <= x:
        dp[i+1][0] = min(dp[i+1][0],dp[i][0] + p)
    dp[i+1][1] = dp[i][0]
    if dp[i][1] <= x:
        dp[i+1][1] = min(dp[i+1][1],dp[i][1]+ p)
        
if dp[n][0] != INF or dp[n][1] != INF:
    print("Kkeo-eok")
else:
    print("Zzz")