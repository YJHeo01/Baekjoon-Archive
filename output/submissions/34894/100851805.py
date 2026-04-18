n = int(input())

arr = list(input())

a = list(map(int,input().split()))

d = dict()

d['U'] = 0
d['O'] = 1
d['S'] = 2
d['P'] = 3
d['C'] = 4

INF = int(1e10)

dp = [[INF]*6 for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
  for j in range(6):
    dp[i+1][j] = dp[i][j]
  dp[i+1][d[arr[i]]+1] = min(dp[i+1][d[arr[i]]+1],dp[i][d[arr[i]]]+a[i])

answer = dp[n][5]

if answer >= INF: answer = -1

print(answer)