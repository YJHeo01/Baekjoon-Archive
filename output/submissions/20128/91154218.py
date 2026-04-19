import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

INF = 9000000000000000

distance = [[INF]*2 for _ in range(n+1)]

distance[1][0] = 0

q = []

heapq.heappush(q,(0,1,0))

while q:
    dist, x, mod = heapq.heappop(q)
    if dist > distance[x][mod]: continue
    for nx, dd in graph[x]:
        nd = dist + dd
        if nd > distance[nx][nd%2]: continue
        distance[nx][nd%2] = nd
        heapq.heappush(q,(nd,nx,nd%2))

for i in range(1,n+1):
    for j in range(2):
        if distance[i][j] >= INF: distance[i][j] = -1
    distance[i][0], distance[i][1] = distance[i][1], distance[i][0]
    print(*distance[i])