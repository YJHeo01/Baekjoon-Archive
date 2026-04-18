import sys, heapq

input = sys.stdin.readline

n,m,k,s,t = map(int,input().split())

edges = [[] for _ in range(k+1)]

graph = [[] for _ in range(n+1)]


for i in range(m):
    u,v,c,o = map(int,input().split())
    edges[o].append((u,v,c))

INF = int(1e18)

distance = [INF] * (n+1)

for o in range(k,0,-1):
    if edges[o] == []: continue
    for u,v,c in edges[o]:
        graph[u].append((v,c,o))
        graph[v].append((u,v,o))
    q = []

    heapq.heappush(q,(0,s))

    distance[s] = 0

    while q:
        dist, x = heapq.heappop(q)
        if dist > distance[x]: continue
        for nx, nc, no in graph[x]:
            if dist % no != 0: continue
            nd = dist + nc
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

answer = distance[t]

if answer == INF: answer = -1

print(answer)