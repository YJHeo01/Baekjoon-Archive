n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]

size = [matrix[0][0]]

for r,c in matrix:
    size.append(c)

INF = int(1e18)

dp = [[INF]*n for _ in range(n)]

for i in range(n): dp[i][i] = 0

for length in range(1,n):
    for i in range(n-length):
        j = i + length
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + size[i]*size[k+1]*size[j+1])
    
answer = dp[0][n-1]

print(answer)