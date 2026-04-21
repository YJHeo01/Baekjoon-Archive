import sys
input = sys.stdin.readline
from collections import deque
INF = 300001
n,m,k,x = map(int,input().split())
city = []
visited = [INF]*(n+1)
graph = [ [] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == INF:
                visited[i] = visited[v] + 1
                queue.append(i)

bfs(graph,visited,x)

for i in range(1,n+1):
    if visited[i] == k:
        city.append(i)

if city == []:
    print("-1")
else:
    l = len(city)
    for i in range(l):
        print(city[i])