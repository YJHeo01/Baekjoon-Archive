N, M, R = map(int,input().split())

visited = [0]*(N+1)
graph = [[] for _ in range(M+1)]
for i in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[v].sort()
    graph[u].sort()

def dfs(V,E,R):
    print(R)
    V[R] = 1
    for i in E[R]:
        if V[i] == 0:
            dfs(V,E,i)
    return 0
print(dfs(visited,graph,1))