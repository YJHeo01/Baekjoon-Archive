import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def main():
    n,query = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        p,q,r = map(int,input().split())
        graph[p].append((q,r))
        graph[q].append((p,r))
    visited = [False] * (n+1)
    for _ in range(query):
        k,v = map(int,input().split())
        print(solution(graph,visited,k,v)-1)

def solution(graph,visited,usado,vx):
    visited[vx] = True
    ret_value = 1
    for nx, r in graph[vx]:
        if visited[nx] == True or usado > r: continue
        ret_value += solution(graph,visited,usado,nx)
    visited[vx] = False
    return ret_value

if __name__ == "__main__":
    main()