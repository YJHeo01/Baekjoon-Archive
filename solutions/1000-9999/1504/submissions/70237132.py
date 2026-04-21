import heapq
import sys

input = sys.stdin.readline

n,e = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int,input().split())

INF = int(1e9)

def dijkstra(start,end):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for v in graph[now]:
            if distance[v[0]] > distance[now] + v[1]:
                distance[v[0]] = distance[now] + v[1]
                heapq.heappush(q,(v[1],v[0]))
    return distance[end]

answer = min(dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n),dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n))

if answer >= INF:
    answer = -1

print(answer)