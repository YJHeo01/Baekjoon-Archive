import sys

input = sys.stdin.readline
INF = int(1e9)
n,m = map(int,input().split())

adj_matrix = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    adj_matrix[a][b] = c
    adj_matrix[b][a] = c


answer = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        answer[i][j] = j
        for k in range(1,n+1):
            if adj_matrix[i][k] + adj_matrix[k][j] >= adj_matrix[i][j]:
                continue
            adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
            if adj_matrix[i][k] < adj_matrix[i][answer[i][j]]:
                answer[i][j] = k

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            print("-",end=" ")
        else:
            print(answer[i][j],end=" ")
    print()