import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

adj_matrix = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    adj_matrix[i][i] = 0

for _ in range(m):
    u,v,b = map(int,input().split())
    adj_matrix[u][v] = 0
    if b == 1:
        adj_matrix[v][u] = 0
    else:
        adj_matrix[v][u] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][k]+adj_matrix[k][j])

k = int(input())

for _ in range(k):
    s,e = map(int,input().split())
    print(adj_matrix[s][e])