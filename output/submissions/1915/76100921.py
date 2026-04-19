import sys

input = sys.stdin.readline

n,m = map(int,input().split())

box = []

for _ in range(n):
    tmp = list(input())
    for i in range(m):
        tmp[i] = int(tmp[i])
    box.append(tmp)

dp = [[[0]*2 for _ in range(m)]for _ in range(n)]

for i in range(m):
    dp[n-1][i][0] = box[n-1][i]


for i in range(n-2,-1,-1):
    for j in range(m):
        if box[i][j] != 0:
            dp[i][j][0] = dp[i+1][j][0] + 1

for i in range(n):
    dp[i][m-1][1] = box[i][m-1]

for i in range(n):
    for j in range(m-2,-1,-1):
        if box[i][j] != 0:
            dp[i][j][1] = dp[i][j+1][1] + 1
    
answer = 0

for x1 in range(n):
    for y1 in range(m):
        if box[x1][y1] == 0:
            continue
        length = min(dp[x1][y1][0],dp[x1][y1][1])
        if length <= answer:
            continue
        square = True
        x2 = x1 + length
        y2 = y1 + length
        for i in range(x1,x2):
            for j in range(y1,y2):
                if box[i][j] == 0:
                    square = False
                    break
        if square == True:
            answer = length

answer = answer ** 2

print(answer)