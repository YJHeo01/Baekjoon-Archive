from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    indegree[b] += 1
    if c == 7: c += 1
    graph[a].append((b,c))
    
queue = deque([])

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)
        
date = [1] * (n+1)

while queue:
    x = queue.popleft()
    for nx, w in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0: queue.append(nx)
        date[nx] = max(date[nx],date[x]+w)

answer = max(date)

print(answer)