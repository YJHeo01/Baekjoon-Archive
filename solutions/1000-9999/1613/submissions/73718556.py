from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int,input().split())

history_graph = [[]for _ in range(n+1)]
reverse_history_graph = [[] for _ in range(n+1)]

for _ in range(k):
    a,b = map(int,input().split())
    history_graph[a].append(b)
    reverse_history_graph[b].append(a)

s = int(input())

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == False:
                visited[nx] = True
                queue.append(nx)

for _ in range(s):
    visited = [False] * (n+1)
    a,b = map(int,input().split())
    bfs(history_graph,visited,a)
    if visited[b] == True:
        print(-1)
        continue
    bfs(reverse_history_graph,visited,a)
    if visited[b] == True:
        print(1)
    else:
        print(0)