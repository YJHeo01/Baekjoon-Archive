import sys

input = sys.stdin.readline

n,k = map(int,input().split())

INF = int(1e9)

adj_matrix = [[INF]*(n+1)for _ in range(n+1)]

for _ in range(k):
    a,b = map(int,input().split())
    adj_matrix[a][b] = 1

for x in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][x]+adj_matrix[x][j])

s = int(input())

for _ in range(s):
    a,b = map(int,input().split())
    if adj_matrix[a][b] < INF:
        print(-1)
    elif adj_matrix[b][a] < INF:
        print(1)
    else:
        print(0)