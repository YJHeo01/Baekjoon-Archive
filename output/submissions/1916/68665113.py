import sys
import heapq
input = sys.stdin.readline
INF = 100001
n = int(input())
m = int(input())

graph = [[]for _ in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start, end = map(int,input().split())

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        distance[node] = dist
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
print(distance[end])
