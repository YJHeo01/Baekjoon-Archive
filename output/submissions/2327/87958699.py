import sys

input = sys.stdin.readline

h,n = map(int,input().split())

dp = [0] * (h+1)
dp[0] = 1000000

for _ in range(n):
    hi,si = map(int,input().split())
    if hi > h: continue
    for j in range(h,-1,-1):
        if j - hi < 0: break
        if dp[j-hi] == 0: continue
        dp[j] = max(dp[j],min(dp[j-hi],si))

print(dp[h])