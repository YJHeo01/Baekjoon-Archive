import sys

sys.setrecursionlimit(4*10**6)
input = sys.stdin.readline

def main():
    n,a,b = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v); graph[v].append(u)
    visited = [False] * (n+1)
    answer = dfs(graph,visited,a,b) - 2
    print(answer)

def dfs(graph,visited,vx,target):
    if target == vx: return 1
    ret_value = 0
    for nx in graph[vx]:
        if visited[nx] == False:
            visited[nx] = True
            ret_value += dfs(graph,visited,nx,target)
    if ret_value != 0: ret_value += 1
    return ret_value

if __name__ == "__main__":
    main()