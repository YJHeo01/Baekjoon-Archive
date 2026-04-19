import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(k):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))


dp = [[-1]*(n+1) for _ in range(m)]

for i in range(m):
    dp[i][1] = 0

for vx in range(1,n+1):
    if dp[0][vx] == -1:
        continue
    for nx, score in graph[vx]:
        if nx < vx:
            continue
        for i in range(1,m):
            dp[i][nx] = max(dp[i][nx],dp[i-1][vx] + score)

print(dp[m-1][n])