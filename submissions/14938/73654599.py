n,m,r = map(int,input().split())

area_item = [0] + list(map(int,input().split()))

INF = int(1e9)

adj_matrix = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a,b,l = map(int,input().split())
    adj_matrix[a][b] = l
    adj_matrix[b][a] = l
for i in range(n+1):
    adj_matrix[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][k]+adj_matrix[k][j])

answer = 0

for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        if adj_matrix[i][j] <= m:
            tmp += area_item[j]
    answer = max(answer,tmp)

print(answer)