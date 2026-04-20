n, m = map(int,input().split())

mirror = [[0]*(m+1)]

for _ in range(n):
    mirror.append([0] + list(map(int,input().split())))

distance = n+m

dp = [[0]*(m+1) for _ in range(n+1)]


i = 1

while i <= distance:
    for j in range(i+1):
        if j > n or (i-j) > m:
            continue
        dp[j][i-j] = mirror[j][i-j] + max(dp[j][i-j-1],dp[j-1][i-j],dp[j-1][i-j-1])
    i += 1

print(dp[n][m])