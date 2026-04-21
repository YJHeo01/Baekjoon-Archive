import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

adj_matrix = [[INF]*(n+1)]
adj_graph = [[]for _ in range(n+1)]
for _ in range(m):
    u,v,b = map(int,input().split())
    adj_graph[u].append((v,0))
    if b == 1:
        adj_graph[v].append((u,0))
    else:
        adj_graph[v].append((u,1))

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        vd, vx = heapq.heappop(q)
        if vd > distance[vx]:
            continue
        for nx, dx in graph[vx]:
            if distance[nx] > distance[vx] + dx:
                distance[nx] = distance[vx] + dx
                heapq.heappush(q,(distance[nx],nx))

for i in range(1,n+1):
    distance = [INF] * (n+1)
    dijkstra(adj_graph,distance,i)
    adj_matrix.append(distance)

k = int(input())

for _ in range(k):
    s,e = map(int,input().split())
    print(adj_matrix[s][e])