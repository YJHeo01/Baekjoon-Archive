import sys

input = sys.stdin.readline

INF = 101

n = int(input())

adj_matrix = [[INF]*(n+1) for _ in range(n+1)]

m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    adj_matrix[a][b] = 1

for i in range(1,n+1):
    adj_matrix[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][k]+adj_matrix[k][j])

for i in range(1,n+1):
    answer = 0
    for j in range(1,n+1):
        if adj_matrix[i][j] >= INF and adj_matrix[j][i] >= INF:
            answer += 1
    print(answer)