n,e = map(int,input().split())

INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

v1, v2 = map(int,input().split())

answer = graph[1][v1] + graph[v1][v2] + graph[v2][n]

if answer >= INF:
    print("-1")
else:print(answer)