n,k = map(int,input().split())

S = list(input())

dp = [[0]*(n+1) for _ in range(k)]

dp[0][0] = 1

INF = 1000000007

for i in range(1,k):
    tmp = 0
    for j in range(n):
        if S[j] == '0':
            dp[i][j+1] += dp[i-1][j]
        else:
            tmp += dp[i-1][j]
            dp[i][j+1] += tmp
        dp[i][j+1] %= INF

answer = 0

for i in range(n):
    if i != n - 1 and S[i] == '0': continue
    answer += dp[k-1][i]
    answer %= INF

print(answer)