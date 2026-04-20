import sys
import heapq


INF = int(1e9)

input = sys.stdin.readline

n,m = map(int,input().split())

road = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

def dijkstra(graph,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for v in graph[now]:
            if distance[v[0]] > distance[now] + v[1]:
                distance[v[0]] = distance[now] + v[1]
                heapq.heappush(q,(v[1],v[0]))

for _ in range(m):
    a,b,c = map(int,input().split())
    road[a].append((b,c))
    road[b].append((a,c))

dijkstra(road,1)

print(distance[n])