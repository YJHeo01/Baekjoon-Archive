import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c,d = map(int,input().split())
    graph[a].append((b,c,d))
    graph[b].append((a,c,d))
    
answer = -1

left, right = 0, int(1e9)

def dijkstra(graph,distance,time):
    q = []
    distance[1] = time
    heapq.heappush(q,(time,1))
    while q:
        dist, x = heapq.heappop(q)
        if dist > distance[x]: continue
        for nx, dd, limit in graph[x]:
            nd = dist + dd
            if nd > min(limit,distance[nx]): continue
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))

INF = int(1e18)

while left <= right:
    mid = (left+right) // 2
    distance = [INF] * (n+1)
    dijkstra(graph,distance,mid)
    if distance[n] < INF:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(answer)
    