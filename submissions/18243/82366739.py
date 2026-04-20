from collections import deque
import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    big = True
    for i in range(1,n+1):
        visited = [INF] * (n+1)
        if 6 >= get_max_distance(graph,visited,i):
            big = False
            break
    if big == True:
        print("Big World!")
    else:
        print("Small World!")

def get_max_distance(graph,visited,start):
    queue = deque([start])
    visited[0] = 0
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == INF:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
    return max(visited)

if __name__ == "__main__":
    INF = int(1e9)
    main()