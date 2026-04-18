import sys, heapq

input = sys.stdin.readline

n,m,k,s,t = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,c,o = map(int,input().split())
    graph[u].append((v,c,o))
    graph[v].append((u,c,o))
    
INF = int(1e18)

distance = [[INF]*k for _ in range(n+1)]

q = []

heapq.heappush(q,(0,s,0))

distance[s][0] = 0

while q:
    dist, x, o = heapq.heappop(q)
    if dist > distance[x][o]: continue
    for nx, nc, no in graph[x]:
        if dist % no != 0: continue
        nd = dist + nc
        if distance[nx][nd%k] > nd:
            distance[nx][nd%k] = nd
            heapq.heappush(q,(nd,nx,nd%k))

answer = min(distance[t])

if answer == INF: answer = -1

print(answer)
        