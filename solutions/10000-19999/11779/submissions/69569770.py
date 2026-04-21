import heapq
import sys
INF = int(1e9)

input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    start,end,cost = map(int,input().split())
    bus[start].append((cost,end))

distance = [INF] * (n+1)
city = [[] for _ in range(n+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    city[start].append(start)
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in bus[now]:
            cost = i[0] + dist
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))
                city[i[1]] = city[now] + [i[1]]
start,end = map(int,input().split())

dijkstra(start)
print(distance[end])
print(len(city[end]))
for i in city[end]:
    print(i,end=" ")
