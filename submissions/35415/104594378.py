import sys, heapq

input = sys.stdin.readline

n,m,k,t = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = int(1e18)

dist_s_m = [INF] * (n+1)
dist_m_e = [INF] * (n+1)

def dijkstra(graph,distance,start):
    q = [(0,start)]
    distance[start] = 0
    while q:
        d, x = heapq.heappop(q)
        if d != distance[x]: continue
        for nx,dd in graph[x]:
            nd = d + dd
            if nd >= distance[nx]: continue
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))
    return distance

dijkstra(graph,dist_s_m,1)
dijkstra(graph,dist_m_e,n)

answer = dist_s_m[k] + dist_m_e[k]

for i in range(1+1,n):
    if dist_m_e[n] + dist_s_m[k] >= answer: continue
    if dist_m_e[n] >= INF or dist_s_m[k] >= INF: continue
    distance = [INF] * (n+1)
    dijkstra(graph,distance,i)
    if t < distance[k]: continue
    tmp = dist_s_m[k] + distance[n] + t - distance[k]
    answer = min(tmp,answer)

if answer >= INF: answer = -1

print(answer)