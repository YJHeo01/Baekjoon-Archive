import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def dijkstra(graph,distance,start,path,block_road):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if block_road[vx][nx] == True:
                continue
            if distance[nx] > dist + length:
                path[nx] = vx
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))

def block_road_func(path,block_road):
    vx = d
    while True:
        nx = path[vx]
        block_road[nx][vx] = True
        vx = nx
        if vx == s:
            break

while True:
    n,m = map(int,input().split())
    if n == 0:
        break
    s,d = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v,p = map(int,input().split())
        graph[u].append((v,p))
    distance = [INF] * n
    path = [0] * n
    block_road = [[False]*n for _ in range(n)]
    dijkstra(graph,distance,s,path,block_road)
    original_length = distance[d]
    block_road_func(path,block_road)
    while True:
        distance = [INF] * n
        path = [0] * n
        dijkstra(graph,distance,s,path,block_road)
        new_length = distance[d]
        if new_length != original_length:
            break
        block_road_func(path,block_road)
    answer = new_length
    if answer >= INF:
        answer = -1
    print(answer)