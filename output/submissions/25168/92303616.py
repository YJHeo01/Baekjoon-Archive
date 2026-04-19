import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    if c == 7: c += 1
    graph[a].append((b,c))
    
date = [1] * (n+1)

for x in range(1,n+1):
    for nx, w in graph[x]:
        date[nx] = max(date[nx],date[x]+w)

answer = max(date)

print(answer)