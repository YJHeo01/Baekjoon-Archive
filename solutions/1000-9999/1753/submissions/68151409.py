import heapq
#import sys

INF = int(1e9)

#input = sys.stdin.readline

v, e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
for i in range(e):
    u,v_,w = map(int,input().split())
    graph[u].append((v_,w))

def djikstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost <= distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

djikstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else: print(distance[i])