import sys

sys.setrecursionlimit(10**6+10)
input = sys.stdin.readline

def main():
    n = int(input())
    node_value = [0] + list(map(int,input().split()))
    distance = [-1] * (n+1)
    distance[1] = 0
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for i in range(2,n+1):
        p,c = map(int,input().split())
        graph[i].append((p,c))
        graph[p].append((i,c))
    answer = n - dfs(graph,node_value,visited,distance,1)
    print(answer)

def dfs(graph,node_value,visited,distance,vx):
    if distance[vx] > node_value[vx]: return 0
    visited[vx] = True
    ret_value = 1
    for nx, dd in graph[vx]:
        if visited[nx]: continue
        visited[nx] = True
        distance[nx] = distance[vx] + dd
        ret_value += dfs(graph,node_value,visited,distance,nx)
    return ret_value

if __name__ == "__main__":
    main()