n = int(input())

max_dp = [[0] * 3 for _ in range(n+1)]
min_dp = [[0] * 3 for _ in range(n+1)]
game = []

for _ in range(n):
    game.append(list(map(int,input().split())))

for i in range(1,n+1):
    max_dp[i][0] = max(max_dp[i-1][0],max_dp[i-1][1]) + game[i-1][0]
    max_dp[i][1] = max(max_dp[i-1]) + game[i-1][1]
    max_dp[i][2] = max(max_dp[i-1][1],max_dp[i-1][2]) +game[i-1][2]
    min_dp[i][0] = min(min_dp[i-1][0],min_dp[i-1][1]) + game[i-1][0]
    min_dp[i][1] = min(min_dp[i-1]) + game[i-1][1]
    min_dp[i][2] = min(min_dp[i-1][1],min_dp[i-1][2]) +game[i-1][2]

print(max(max_dp[n]),min(min_dp[n]))