import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

adj_matrix_A = [[INF]*(n+1) for _ in range(n+1)]
adj_matrix_B = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    adj_matrix_A[i][i] = 0
    adj_matrix_B[i][i] = 0

for _ in range(m):
    a,b = map(int,input().split())
    adj_matrix_A[a][b] = 1
    adj_matrix_B[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            adj_matrix_A[i][j] = min(adj_matrix_A[i][j],adj_matrix_A[i][k]+adj_matrix_A[k][j])
            adj_matrix_B[i][j] = min(adj_matrix_B[i][j],adj_matrix_B[i][k]+adj_matrix_B[k][j])
answer = n

for i in range(1,n+1):
    for j in range(1,n+1):
        if adj_matrix_A[i][j] >= INF and adj_matrix_B[i][j] >= INF:
            answer -= 1
            break
print(answer)