import sys

input = sys.stdin.readline

n,m,power,hp = map(int,input().split())

dp = [[[False]*301 for _ in range(301)] for _ in range(m+1)]

dp[0][0][0] = True

max_value = [0] * 301

for _ in range(n):
    x,y = map(int,input().split())
    for k in range(m,0,-1):
        for i in range(300,-1,-1):
            for j in range(300,-1,-1):
                if dp[k-1][i][j]:
                    nx = min(300,i + x)
                    ny = min(300,j + y)
                    dp[k][nx][ny] = True
                    max_value[nx] = max(max_value[nx],ny)

k = int(input())

monster = [list(map(int,input().split())) for _ in range(k)]

answer = 0

for x in range(301):
    y = max_value[x]
    tmp = 0
    for a,b in monster:
        if x+power >= a and y+hp >= b:tmp += 1
    answer = max(answer,tmp)
    
print(answer)