N, M, R = map(int,input().split())

visited = [0]*(N+1)
graph = [[] for _ in range(M+1)]
for i in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(V,E,R):
    print(R)
    V[R] = 1
    while(1):
        if E[R] == [] : return 0
        tmp = min(E[R])
        E[R].remove(tmp)
        if V[tmp] == 0 : dfs(V,E,tmp)
print(dfs(visited,graph,1))