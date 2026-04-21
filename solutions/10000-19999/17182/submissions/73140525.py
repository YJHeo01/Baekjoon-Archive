n, k = map(int,input().split())

adj_matrix = []

for _ in range(n):
    adj_matrix.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        for x in range(n):
            adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][x]+adj_matrix[x][j])

answer = 0

visited = [False] * n

start = k
INF = int(1e9)

while True:
    visited[start] = True
    min_distance = INF
    for i in range(n):
        if visited[i] == True:
            continue
        if adj_matrix[start][i] < min_distance:
            min_distance = adj_matrix[start][i] 
            end = i
    if min_distance == INF:
        break
    answer += min_distance
    start = end

print(answer)