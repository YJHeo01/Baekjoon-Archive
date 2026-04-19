import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

v,e,p = map(int,input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance_start = [INF] * (v+1)
distance_minjun = [INF] * (v+1)

def dijkstra(graph,distance,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        vd, vx = heapq.heappop(q)
        if distance[vx] > vd:
            continue
        for nx, length in graph[vx]:
            if distance[nx] > vd + length:
                distance[nx] = vd + length
                heapq.heappush(q,(distance[nx],nx))
    
dijkstra(graph,distance_start,1)
dijkstra(graph,distance_minjun,p)

if distance_start[v] == distance_start[p] + distance_minjun[v]:
    print("SAVE HIM")
else:
    print("GOOD BYE")