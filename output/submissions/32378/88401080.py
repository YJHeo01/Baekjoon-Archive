import sys

input = sys.stdin.readline

n,k,s = map(int,input().split())
grow = list(map(int,input().split()))
    
if k > 36: print("MEGA"); exit(0)

dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = s
    
for i in range(n):
    for j in range(k):
        if dp[i][j] <= 0: continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + grow[i])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] * 2)
    if dp[i][k] > 0: dp[i+1][k] = max(dp[i+1][k],dp[i][k]+grow[i])

mascot_size = max(dp[n])

if mascot_size > 10 ** 11:
    print("MEGA")
elif mascot_size <= 0:
    print("-1")
else:
    print(mascot_size)