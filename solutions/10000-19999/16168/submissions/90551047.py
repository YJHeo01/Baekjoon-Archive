import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

yes = False

v,e = map(int,input().split())

visited = [False] * e

graph = [[] for _ in range(v+1)]

for i in range(e):
    a,b = map(int,input().split())
    graph[a].append((b,i))
    graph[b].append((a,i))

def dfs(graph,visited,x,cnt):
    if cnt == e: return True
    ret_value = False
    for nx, i in graph[x]:
        if visited[i]: continue
        visited[i] = True
        ret_value |= dfs(graph,visited,nx,cnt+1)
        visited[i] = False
    return ret_value
        

yes = dfs(graph,visited,1,0)
    
if yes:
    print("YES")
else:
    print("NO")
