import sys

input = sys.stdin.readline

n = int(input())

dp = [[0]*6 for _ in range(n+1)]

max_cnt = 0
max_grade = 0

for i in range(n):
    a,b = map(int,input().split())
    dp[i+1][a] = dp[i][a] + 1
    dp[i+1][b] = dp[i][b] + 1
    for j in range(6):
        if dp[i+1][j] > max_cnt or (dp[i+1][j]==max_cnt and max_grade > j):
            max_cnt = dp[i+1][j]
            max_grade = j

print(max_cnt,max_grade)