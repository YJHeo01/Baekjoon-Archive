import sys
from collections import deque

sys.stdin.readline

n,a,b = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited_a = [False] * (n+1)
visited_b = [False] * (n+1)

def bfs(graph,visited,start,finish):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if visited[nx] or nx == start or nx == finish: continue
            visited[nx] = True
            queue.append(nx)

bfs(graph,visited_a,a,b)
bfs(graph,visited_b,b,a)

answer = 0

for i in range(1,n+1):
    if visited_a[i] and visited_b[i]: answer += 1

print(answer)