import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

INF = int(1e10)

roads = [list(map(int,input().split())) for _ in range(m)]

shortest_path = [[INF]*n for _ in range(n)]

road_id = [[-1]*n for _ in range(n)]

graph = [[] for _ in range(n)]

for i in range(n):
    shortest_path[i][i] = 0

for i in range(m):
    a,b,c = roads[i]
    shortest_path[a][b] = c
    shortest_path[b][a] = c
    road_id[a][b] = i
    road_id[b][a] = i
    graph[b].append((a,c))
    graph[a].append((b,c))

for k in range(n):
    for i in range(n):
        for j in range(n):
            shortest_path[i][j] = min(shortest_path[i][j],shortest_path[i][k]+shortest_path[k][j])
            

def dijkstra(graph,start):
    q = []
    distance = [INF] * n
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, dd in graph[vx]:
            if road_id[vx][nx] == road_idx: continue
            nd = dist + dd
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))
    return distance

for road_idx in range(m):
    answer = 0
    tmp = []
    for start in range(n):
        tmp.append(dijkstra(graph,start))
    for i in range(n):
        for j in range(i):
            if shortest_path[i][j] != tmp[i][j]: answer += 1
    print(answer,end=" ")