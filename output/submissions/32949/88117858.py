import sys

input = sys.stdin.readline

n,t = map(int,input().split())

r = [[] for _ in range(101)]

for _ in range(n):
    s,p,h = map(int,input().split())
    r[s].append((p,h))

dp = [[-1]*(t+1) for _ in range(101)]

dp[0][0] = 0

for p,h in r[0]:
    for i in range(t,p-1,-1):
        if dp[0][i-p] == -1: continue
        dp[0][i] = max(dp[0][i],dp[0][i-p]+h)
        
answer = max(dp[0])

for i in range(1,101):
    for p,h in r[i]:
        for j in range(t,p,-1):
            if dp[i][j-p] != -1:
                dp[i][j] = max(dp[i][j],dp[i][j-p]+h)
            if dp[i-1][j-p] != -1:
                dp[i][j] = max(dp[i][j],dp[i-1][j-p]+h)
    answer = max(answer,max(dp[i]))
    
print(answer)