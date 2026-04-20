import sys

input = sys.stdin.readline

n,t,m = map(int,input().split())

s,e = map(int,input().split())

INF = int(1e9)

edges = [[]*n for _ in range(t)]

for i in range(t):
    for _ in range(m):
        a,b,c = map(int,input().split())
        edges[i].append((a,b,c))
    
dp = [[INF]*n for _ in range(t+1)]

dp[0][s] = 0

for i in range(t):
    for j in range(n):
        dp[i+1][j] = dp[i][j]
    for a,b,c in edges[i]:
        dp[i+1][b] = min(dp[i+1][b],dp[i][a]+c)
        dp[i+1][a] = min(dp[i+1][a],dp[i][b]+c)

answer = dp[t][e]

if answer >= INF: answer = -1

print(answer)