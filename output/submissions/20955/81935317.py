import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6+1)

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [-1] * (n+1)
    answer = -1
    for i in range(1,n+1):
        if visited[i] == -1:
            visited[i] = 0
            answer += 1
            answer += dfs(graph,visited,i)
    print(answer)

def dfs(graph,visited,vx):
    ret_value = 0
    for nx in graph[vx]:
        if visited[nx] == 0 and visited[vx] != 1:
            ret_value += 1
            continue
        if visited[nx] != -1: continue
        visited[nx] = visited[vx] + 1
        ret_value += dfs(graph,visited,nx)
    return ret_value

if __name__ == "__main__":
    main()