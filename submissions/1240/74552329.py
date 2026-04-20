import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

distance = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    distance[a][b] = c
    distance[b][a] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])

for _ in range(m):
    a,b = map(int,input().split())
    print(distance[a][b])