from collections import deque
import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
    visited = [-1] * (n+1)
    bfs(graph,visited)
    print(visited[n])

def bfs(graph,visited):
    queue = deque([1])
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == -1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

if __name__ == "__main__":
    main()