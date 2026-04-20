import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = dp[i][j]
            if array[i][j] >= 0: dp[i+1][j+1] += array[i][j]
            if i != 0 and array[i-1][j] >= 0: dp[i+1][j+1] += array[i-1][j]
            if j != 0 and array[i][j-1] >= 0: dp[i+1][j+1] += array[i][j-1]
    answer = -2000
    for i in range(n):
        target = m - 1
        left, right = 0,m-1
        while left <= right:
            mid = (left+right) // 2
            if array[i][mid] >= 0:
                target = mid
                right = mid - 1
            else:
                left = mid + 1
        answer = max(answer,dp[n][m]-dp[i][target])
    print(answer)