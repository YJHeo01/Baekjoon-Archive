import sys,heapq

input = sys.stdin.readline

V,e = map(int,input().split())

INF = int(1e10)

road_list = [[] for _ in range(V+1)]

for _ in range(e):
    u,v,w = map(int,input().split())
    road_list[u].append((v,w))
    road_list[v].append((u,w))
house = [True] * (V+1)

m,x = map(int,input().split())
Mcdonald = list(map(int,input().split()))

for idx in Mcdonald:
    house[idx] = False

s,y = map(int,input().split())
starbucks = list(map(int,input().split()))

for idx in starbucks:
    house[idx] = False

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, nd in graph[vx]:
            if distance[nx] > distance[vx] + nd:
                distance[nx] = distance[vx] + nd
                heapq.heappush(q,(distance[nx],nx))

answer = INF     
for i in range(1,V+1):
    if house[i] == True:
        distance = [INF] * (V+1)
        dijkstra(road_list,distance,i)
        starbucks_distance, Mcdonald_distance = INF, INF
        for idx in starbucks:
            if distance[idx] > y:
                continue
            starbucks_distance = min(starbucks_distance,distance[idx])
        if starbucks_distance >= INF:
            continue
        for idx in Mcdonald:
            if distance[idx] > x:
                continue
            Mcdonald_distance = min(Mcdonald_distance,distance[idx])
        if Mcdonald_distance >= INF:
            continue
        if answer > starbucks_distance + Mcdonald_distance:
            answer = starbucks_distance + Mcdonald_distance

if answer >= INF:
    answer = -1
print(answer)