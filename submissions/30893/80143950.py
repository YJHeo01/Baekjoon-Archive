import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def main():
    global e
    n,s,e = map(int,input().split())
    graph = get_graph(n)
    visited = [-1] * (n+1)
    visited[s] = 0
    dfs(graph,visited,s)
    if visited[e] % 2 == 0:
        print("Second")
    else:
        print(reverse_dfs(graph,visited,e))

def get_graph(n):
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def dfs(graph,visited,vx):
    for nx in graph[vx]:
        if visited[nx] == -1:
            visited[nx] = visited[vx] + 1
            dfs(graph,visited,nx)

def reverse_dfs(graph,visited,vx):
    if visited[vx] % 2 == 1 and len(graph[vx]) > 2 and vx != e:
        return "Second"
    if visited[vx] == 0:
        return "First"
    for nx in graph[vx]:
        if visited[nx] == visited[vx] - 1: return reverse_dfs(graph,visited,nx)

if __name__ == "__main__":
    main()