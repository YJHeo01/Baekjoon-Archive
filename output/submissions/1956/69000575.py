import sys

input = sys.stdin.readline

INF = int(1e9)
v, e =map(int,input().split())

town = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    town[a][b] = c

for i in range(1,v+1):
    for j in range(1,v+1):
        for k in range(1,v+1):
            town[j][k] = min(town[j][k],town[j][i]+town[i][k])

answer = INF

for i in range(1,v+1):
    answer = min(answer,town[i][i])

if answer == INF:
    answer = -1

print(answer)
