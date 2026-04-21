import sys

input = sys.stdin.readline

INF = int(1e9)

n,m,x = map(int,input().split())

time = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    start, end, t = map(int,input().split())
    time[start][end] = t

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            time[j][k] = min(time[j][k],time[j][i]+time[i][k])
answer = 0
for i in range(1,n+1):
    answer = max(answer,time[i][x]+time[x][i])

print(answer)