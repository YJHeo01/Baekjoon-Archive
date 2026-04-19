import sys

input = sys.stdin.readline

n,m = map(int,input().split())

array = [list(input().rstrip()) for _ in range(n)]

dp = [[0]*(m+2) for _ in range(n+2)]

answer = 0

for y in range(m):
    for x in range(1,n+1):
        dp[x][y+1] = max(dp[x+1][y],dp[x][y],dp[x-1][y]) + int(array[x-1][y])
        answer = max(answer,dp[x][y+1]-int(array[x-1][y]))

print(answer)