import sys

input = sys.stdin.readline

n = int(input())

max_dp = [[0] * 3 for _ in range(2)]
min_dp = [[0] * 3 for _ in range(2)]
game = []

for _ in range(n):
    game = list(map(int,input().split()))
    max_dp[1][0] = max(max_dp[0][0],max_dp[0][1]) + game[0]
    max_dp[1][1] = max(max_dp[0]) + game[1]
    max_dp[1][2] = max(max_dp[0][2],max_dp[0][1]) + game[2]
    min_dp[1][0] = min(min_dp[0][0],min_dp[0][1]) + game[0]
    min_dp[1][1] = min(min_dp[0]) + game[1]
    min_dp[1][2] = min(min_dp[0][1],min_dp[0][2]) + game[2]
    max_dp[0][0], max_dp[0][1], max_dp[0][2] = max_dp[1][0], max_dp[1][1], max_dp[1][2]
    min_dp[0][0], min_dp[0][1], min_dp[0][2] = min_dp[1][0], min_dp[1][1], min_dp[1][2]


print(max(max_dp[1]),min(min_dp[1]))