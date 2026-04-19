n,m = map(int,input().split())

box = []

for _ in range(n):
    tmp = list(input())
    for i in range(m):
        tmp[i] = int(tmp[i])
    box.append(tmp)

dp = [[[0]*4 for _ in range(m)]for _ in range(n)]

for i in range(m):
    dp[0][i][0] = box[0][i]
    dp[n-1][i][1] = box[n-1][i]

for i in range(n):
    for j in range(m):
        if box[i][j] != 0:
            dp[i][j][0] = dp[i-1][j][0] + 1

for i in range(n-2,-1,-1):
    for j in range(m):
        if box[i][j] != 0:
            dp[i][j][1] = dp[i+1][j][1] + 1

for i in range(n):
    dp[i][0][2] = box[i][0]
    dp[i][m-1][3] = box[i][m-1]

for i in range(n):
    for j in range(1,m):
        if box[i][j] != 0:
            dp[i][j][2] = dp[i][j-1][2] + 1

for i in range(n):
    for j in range(m-2,-1,-1):
        if box[i][j] != 0:
            dp[i][j][3] = dp[i][j+1][3] + 1
    
answer = 0

for x1 in range(n):
    for y1 in range(m):
        if box[x1][y1] == 0:
            continue
        max_length = min(dp[x1][y1][1],dp[x1][y1][3])
        for size in range(answer,max_length):
            y2 = y1 + size
            x2 = x1 + size
            if size <= min(dp[x1][y2][2],dp[x1][y2][1],dp[x2][y1][0],dp[x2][y1][3],dp[x2][y2][0],dp[x2][y2][2]):
                answer = size + 1

answer = answer ** 2

print(answer)
