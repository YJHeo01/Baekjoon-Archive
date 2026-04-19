import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j]
            dp[i+1][j+1] += array[i][j]
    answer = array[n-1][m-1]
    for i in range(n):
        for j in range(m):
            answer = max(answer,dp[n][m]+dp[i][j]-dp[i][m]-dp[n][j])
    print(answer)