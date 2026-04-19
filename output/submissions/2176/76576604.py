import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c, = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

node_to_end_distance = [INF] * (n+1)

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        vd, vx = heapq.heappop(q)
        if vd > distance[vx]:
            continue
        for nx, length in graph[vx]:
            nd = vd + length
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

dijkstra(graph,node_to_end_distance,2)

answer = 0

dp = [0] * (n+1)

dp[2] = 1

def dfs(graph,dp,distance,vx):
    for nx, length in graph[vx]:
        if distance[nx] < distance[vx]:
            if dp[nx] != 0:
                dp[vx] += dp[nx]
            else:
                dp[vx] += dfs(graph,dp,distance,nx)
    return dp[vx]

answer = dfs(graph,dp,node_to_end_distance,1)

print(answer)