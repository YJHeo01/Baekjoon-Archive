import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
    
x,z = map(int,input().split())

p = int(input()) + 2

pos = [x] + list(map(int,input().split())) + [z]

adj_matrix = []

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, x = heapq.heappop(q)
        if dist > distance[x]: continue
        for nx, dd in graph[x]:
            nd = dist + dd
            if nd > distance[nx]: continue
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))

for i in range(p):
    start = pos[i]
    INF = int(1e18)
    distance = [INF] * (n+1)
    distance[start] = 0
    dijkstra(graph,distance,start)
    tmp = []
    for j in range(p):
        tmp.append(distance[pos[j]])
    adj_matrix.append(tmp)
    
distance = [[INF]*p for _ in range(1<<p)]

distance[1][0] = 0

q = []

heapq.heappush(q,(0,1,0))

while q:
    dist, bitmask, x = heapq.heappop(q)
    if dist > distance[bitmask][x]: continue
    for nx in range(p):
        if bitmask & (1<<nx) != 0: continue
        if distance[bitmask+(1<<nx)][nx] > dist + adj_matrix[x][nx]:
            distance[bitmask+(1<<nx)][nx] = dist + adj_matrix[x][nx]
            heapq.heappush(q,(dist+adj_matrix[x][nx],bitmask+(1<<nx),nx))
            
answer = distance[(1<<p)-1][p-1]

if answer >= INF: answer = -1

print(answer)