import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

block = [False] * (n+1)

for _ in range(m):
    block[int(input())] = True

dp = [[INF]*1000 for _ in range(n+1)]

dp[1][0] = 0

for x in range(2,n+1):
    if block[x]: continue
    for y in range(1,1000):
        for dy in [1,0,-1]:
            dx = y + dy
            if x - dx < 0: continue
            dp[x][y] = min(dp[x][y],dp[x-y][dx]+1)

answer = min(dp[n])

if answer >= INF: answer = -1

print(answer)