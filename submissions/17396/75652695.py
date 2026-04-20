import sys,heapq

input = sys.stdin.readline

n,m = map(int,input().split())
ward = list(map(int,input().split()))

ward[n-1] = 0

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))

INF = 100000 * 300000 + 1

distance = [INF] * n

def dijkstra(graph,distance,ward):
    q = []
    heapq.heappush(q,(0,0))
    distance[0] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, nd in graph[vx]:
            if ward[nx] == 1:
                continue
            if distance[nx] > dist + nd:
                distance[nx] = dist + nd
                heapq.heappush(q,(distance[nx],nx))

dijkstra(graph,distance,ward)

answer = distance[n-1]

if answer >= INF:
    answer = -1
print(answer)