from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [-1] * (n+1)
    bfs(graph,visited)
    cost = [list(map(int,input().split())) for _ in range(n)]
    answer = int(1e18)
    for i in range(2):
        tmp = 0
        for j in range(n):
            tmp += cost[j][(visited[j]+i)%2]
        answer = min(answer,tmp)
    print(answer)

def bfs(graph,visited):
    queue = deque([0])
    visited[0] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] != -1: continue
            visited[nx] = visited[vx] + 1
            queue.append(nx)
 
if __name__ == "__main__":
    main()