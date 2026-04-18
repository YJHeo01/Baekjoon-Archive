n,m = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]

for x in range(n):
    for y in range(m):
        dp[x+1][y+1] = dp[x+1][y] + dp[x][y+1] + matrix[x][y] - dp[x][y]
        

answer = 0

for x in range(n):
    for y in range(m):
        for dx in range(1,11):
            if x + dx > n: break
            for dy in range(1,11):
                if y + dy > m: break
                tmp = dp[x+dx][y+dy] - dp[x][y+dy] - dp[x+dx][y] + dp[x][y]
                if tmp >= 10:
                    if tmp == 10: answer += 1
                    break

print(answer)