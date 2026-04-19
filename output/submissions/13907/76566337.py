import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

n,m,k = map(int,input().split())

s,d = map(int,input().split())

graph = [[] for _ in range(n+1)]

distance = [[INF]*(n+1) for _ in range(n)]

for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,0,start))
    distance[0][start] = 0
    while q:
        vd, visit_road_cnt, vx = heapq.heappop(q)
        if distance[visit_road_cnt][vx] > vd:
            continue
        for nx, dd in graph[vx]:
            nd = vd + dd
            if distance[visit_road_cnt+1][nx] > nd:
                distance[visit_road_cnt+1][nx] = nd
                heapq.heappush(q,(nd,visit_road_cnt+1,nx))
answer = INF

dijkstra(graph,distance,s)

for i in range(n):
    if answer > distance[i][d]:
        answer = distance[i][d]

print(answer)

for _ in range(k):
    tmp = int(input())
    answer = INF
    for i in range(n):
        distance[i][d] += tmp * i
        if answer > distance[i][d]:
            answer = distance[i][d]
    print(answer)