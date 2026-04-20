import sys
import heapq
input = sys.stdin.readline

n,e = map(int,input().split())

INF = int(1e9)

graph = [[] for i in range(n+1)]

distance = [INF]*(n+1)
answer = 0
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

v1, v2 = map(int,input().split())

dijkstra(1)
answer += distance[v1]
distance = [INF]*(n+1)
dijkstra(v1)
answer += distance[v2]
distance = [INF]*(n+1)
dijkstra(v2)
answer += distance[n]



if answer >= INF:
    print("-1")
else:print(answer)