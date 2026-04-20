import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def main():
    n,s,e = map(int,input().split())
    graph = get_graph(n)
    visited = [-1] * (n+1)
    visited[s] = 0
    answer = ['Second','First']
    dfs(graph,visited,s)
    print(answer[visited[e]%2])

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

if __name__ == "__main__":
    main()