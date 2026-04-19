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
    graph[b].append((a,w))

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,0,start))
    distance[0][start] = 0
    ret_value = [False] * n
    while q:
        vd, visit_road_cnt, vx = heapq.heappop(q)
        if vd > min(distance[visit_road_cnt][vx],distance[visit_road_cnt][d]):
            continue
        if visit_road_cnt == n-1:
            break
        for nx, dd in graph[vx]:
            nd = vd + dd
            if visit_road_cnt >= 1 and distance[visit_road_cnt-1][nx] == vd - dd:
                continue
            if distance[visit_road_cnt+1][nx] > nd:
                distance[visit_road_cnt+1][nx] = nd
                heapq.heappush(q,(nd,visit_road_cnt+1,nx))
    return ret_value

answer = INF

city_cnt_list = dijkstra(graph,distance,s)

length = 0

for i in range(n):
    if answer > distance[i][d]:
        answer = distance[i][d]

print(answer)

for _ in range(k):
    p = int(input())
    answer = INF
    for i in range(n):
        if distance[i][d] == INF:
            continue
        distance[i][d] += p * i
        answer = min(answer,distance[i][d])
    print(answer)