import sys,heapq

input = sys.stdin.readline

n,k = map(int,input().split())
INF = int(1e9)
history_graph = [[]for _ in range(n+1)]
history_array = [[] for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    history_graph[a].append(b)

s = int(input())

def dijkstra(graph,distance,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist,vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        next_dist = dist + 1
        for nx in graph[vx]:
            if distance[nx] > next_dist:
                distance[nx] = next_dist
                heapq.heappush(q,(next_dist,nx))


for _ in range(s):
    a,b = map(int,input().split())
    if history_array[a] == []:
        distance = [INF] * (n+1)
        dijkstra(history_graph,distance,a)
        history_array[a] = distance
    if history_array[a][b] != INF:
        print(-1)
        continue
    if history_array[b] == []:
        distance = [INF] * (n+1)
        dijkstra(history_array,distance,b)
        history_array[b] = distance
    if history_array[b][a] != INF:
        print(1)
    else:
        print(0)