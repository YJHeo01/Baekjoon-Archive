import sys

input = sys.stdin.readline

n,m = map(int,input().split())

INF = int(1e10)

roads = [list(map(int,input().split())) for _ in range(m)]

adj_matrix = [[[INF]*n for _ in range(n)] for _ in range(m)]

shortest_path = [[INF]*n for _ in range(n)]

for i in range(m):
    for j in range(n):
        adj_matrix[i][j][j] = 0

for i in range(n):
    shortest_path[i][i] = 0

for i in range(m):
    a,b,c = roads[i]
    shortest_path[a][b] = c
    shortest_path[b][a] = c
    for j in range(m):
        if i == j: continue
        adj_matrix[j][a][b] = c
        adj_matrix[j][b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            shortest_path[i][j] = min(shortest_path[i][j],shortest_path[i][k]+shortest_path[k][j])
for id in range(m):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj_matrix[id][i][j] = min(adj_matrix[id][i][j],adj_matrix[id][i][k]+adj_matrix[id][k][j])

for k in range(m):
    answer = 0
    for i in range(n):
        for j in range(i):
            if adj_matrix[k][i][j] != shortest_path[i][j]: answer += 1
    print(answer,end=" ")