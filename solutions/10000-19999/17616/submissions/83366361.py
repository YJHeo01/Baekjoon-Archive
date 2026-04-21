from collections import deque
import sys

input = sys.stdin.readline

def main():
    n,m,x = map(int,input().split())
    up_graph = [[] for _ in range(n+1)]
    down_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        up_graph[b].append(a)
        down_graph[a].append(b)
    visited = [False] * (n+1)
    u = 1 + bfs(up_graph,visited,x)
    v = n - bfs(down_graph,visited,x)
    print(u,v)

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == False:
                visited[nx] = True
                cnt += 1
                queue.append(nx)
    return cnt

if __name__ == "__main__":
    main()