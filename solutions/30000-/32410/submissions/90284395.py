import sys

input = sys.stdin.readline

n,m,power,hp = map(int,input().split())

dp = [[-1]*301 for _ in range(301)]

dp[0][0] = 0

max_value = [0] * 301

for i in range(n):
    x,y = map(int,input().split())
    for k in range(m,0,-1):
        for i in range(300,-1,-1):
            if dp[k-1][i] == -1: continue
            dp[k][min(300,i+x)] = max(dp[k-1][i]+y,dp[k][min(300,i+x)])
            max_value[min(300,i+x)] = max(max_value[min(300,i+x)],dp[k][min(300,i+x)])

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