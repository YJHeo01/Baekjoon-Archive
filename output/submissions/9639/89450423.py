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
            if array[i][j] >= 0: dp[i+1][j+1] += array[i][j]
    answer = array[n-1][m-1]
    for i in range(n):
        target = m
        left, right = 0,m-1
        while left <= right:
            mid = (left+right) // 2
            if array[i][mid] >= 0:
                target = mid
                right = mid - 1
            else:
                left = mid + 1
        if target == m: continue
        answer = max(answer,dp[n][m]+dp[i][target]-dp[n][target]-dp[i][m])
    print(answer)