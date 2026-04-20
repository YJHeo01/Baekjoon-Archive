from collections import deque
import sys

input = sys.stdin.readline

def main():
    start,end = map(int,input().split())
    n,m = map(int,input().split())
    graph = get_graph(n,m)
    visited = [INF] * (n+1)
    bfs(graph,visited,start)
    answer = visited[end]
    if answer >= INF: answer = - 1
    print(answer)
    
def get_graph(n,m):
    graph = [[]for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

if __name__ == "__main__":
    INF = int(1e9)
    main()