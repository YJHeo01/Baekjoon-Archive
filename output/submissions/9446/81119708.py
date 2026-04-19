import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    n,m = map(int,input().split())
    cost = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,x,y = map(int,input().split())
        graph[a].append((x,y))
    visited = [False] * (n+1)
    print(dfs(graph,visited,cost,1))

def dfs(graph,visited,cost,vx):
    visited[vx] = True
    ret_value = cost[vx]
    for a,b in graph[vx]:
        if visited[a] == False:
            dfs(graph,visited,cost,a)
        if visited[b] == False:
            dfs(graph,visited,cost,b)
        ret_value = min(ret_value,cost[a]+cost[b])
    cost[vx] = ret_value
    return ret_value

if __name__ == "__main__":
    main()