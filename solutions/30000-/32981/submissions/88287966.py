import sys; input = sys.stdin.readline
INF = int(1e9) + 7
SIZE = int(1e7)
dp = [0] * (SIZE+1)
dp[1] = 5
dp[2] = 20
for i in range(2,SIZE):
    dp[i+1] = dp[i] * 5
    dp[i+1] %= INF
for _ in range(int(input())):
    print(dp[int(input())])