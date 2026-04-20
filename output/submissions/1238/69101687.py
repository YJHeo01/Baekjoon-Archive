import sys

input = sys.stdin.readline

INF = int(9e11)

n,m,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

time = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    start, end, t = map(int,input().split())
    time[start][end] = t

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            time[i][j] = min(time[i][j],time[i][k]+time[k][j])
answer = 0
for i in range(1,n+1):
    answer = max(answer,time[i][x]+time[x][i])

print(answer)