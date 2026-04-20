INF = int(1e19)

import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [INF] * (n+1)

def dijkstra(graph,distance,no):
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist, vx = heapq.heappop(q)
        for nx, dd in graph[vx]:
            if no[nx][vx]: continue
            nd = dd + dist
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))
no = [[False]*(n+1) for _ in range(n+1)]


dijkstra(graph,distance,no)

x = n

while True:
    if x == 1: break
    for nx,dd in graph[x]:
        if distance[nx] + dd == distance[x]:
            no[nx][x] = True
            no[x][nx] = True
            x = nx
            break

distance = [INF] * (n+1)

dijkstra(graph,distance,no)

print(distance[n])