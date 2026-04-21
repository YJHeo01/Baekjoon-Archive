import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

INF = int(1e10)

roads = [list(map(int,input().split())) for _ in range(m)]

shortest_path = [[INF]*n for _ in range(n)]

distance = [[[INF]*n for _ in range(n)] for _ in range(m)]

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


def dijkstra(graph,distance):
    q = []
    for k in range(m):
        for i in range(n):
            distance[k][i][i] = 0
            heapq.heappush(q,(0,i,k,i))
    while q:
        dist, vx, id, start = heapq.heappop(q)
        if dist > distance[id][start][vx]: continue
        for nx, dd in graph[vx]:
            if road_id[vx][nx] == id: continue
            nd = dist + dd
            if distance[id][start][nx] > nd:
                distance[id][start][nx] = nd
                heapq.heappush(q,(nd,nx,id,start))

dijkstra(graph,distance)

for k in range(m):
    answer = 0
    for i in range(n):
        for j in range(i):
            if shortest_path[i][j] != distance[k][i][j]: answer += 1
    print(answer,end=" ")