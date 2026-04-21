import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

t = int(input())

def dijkstra(graph,distance,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist,now  = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nx, nd in graph[now]:
            if distance[nx] > dist + nd:
                distance[nx] = dist + nd
                heapq.heappush(q,(distance[nx],nx))

for _ in range(t):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    distance = [INF] * (n+1)
    dijkstra(graph,distance,c)
    cnt,time = n+1,0
    distance.sort(reverse=True)
    for d in distance:
        if d == INF:
            cnt -= 1
        else:
            time = d
            break
    print(cnt,time)