#https://github.com/YJHeo01/BOJ/blob/main/%EC%97%AD%EC%82%AC%20-%201613%EB%B2%88.py
import sys,heapq

input = sys.stdin.readline

n,k = map(int,input().split())

INF = int(1e9)

adj_matrix = [[INF]*(n+1) for _ in range(n+1)]
adj_graph = [[]for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    adj_graph[a].append(b)

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx in graph[vx]:
            if distance[nx] > dist + 1:
                distance[nx] = dist + 1
                heapq.heappush(q,(distance[nx],nx))

s = int(input())

for _ in range(s):
    a,b = map(int,input().split())
    if adj_matrix[a][a] != 0:
        dijkstra(adj_graph,adj_matrix[a],a)
    if adj_matrix[a][b] < INF:
        print(-1)
        continue
    if adj_matrix[b][b] != 0:
        dijkstra(adj_graph,adj_matrix[b],b)
    if adj_matrix[b][a] < INF:
        print(1)
    else:
        print(0)