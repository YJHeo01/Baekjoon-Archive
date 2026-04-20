INF = int(1e9)

n = int(input())

adj_matrix = [[INF]*n for _ in range(n)]

for i in range(n):
    tmp = list(input())
    for j in range(n):
        if tmp[j] == 'Y':
            adj_matrix[i][j] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][k]+adj_matrix[k][j])
    
answer = 0

for i in range(n):
    tmp = -1
    for j in range(n):
        if adj_matrix[i][j] <= 2:
            tmp += 1
    answer = max(answer,tmp)

print(answer)
