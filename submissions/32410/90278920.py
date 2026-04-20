import sys

input = sys.stdin.readline

INF = 90000

n,m,power,hp = map(int,input().split())

dp = [[-2] * 90001 for _ in range(m+1)]

dpdp = [0] * 301

dp[0][0] = 0

for _ in range(n):
    x,y = map(int,input().split())
    for i in range(m,0,-1):
        for j in range(INF,0,-1):
            if x > j: break
            if dp[i-1][j-x] == -2: continue
            dp[i][j] = max(dp[i][j],dp[i-1][j-x]+y)
            dpdp[min(300,j)] = max(dpdp[min(300,j)],dp[i][j])

k = int(input())

monster = [list(map(int,input().split())) for _ in range(k)]

answer = 0

dpdp = [0] * 301

for x in range(301):
    y = dp[m][x]
    tmp = 0
    for a,b in monster:
        if x+power >= a and y+hp >= b:tmp += 1
    answer = max(answer,tmp)
    
print(answer)