import heapq

n,m = map(int,input().split())

graph = [[]for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,i))
    graph[b].append((a,i))

INF = int(1e9)

time_list = [INF] * (n+1)

def dijkstra(graph,distance):
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nx,time in graph[now]:
            if time >= dist % m:
                next_time = dist - dist % m + time + 1
            else:
                next_time = dist + m - dist % m + time + 1
            if distance[nx] > next_time:
                distance[nx] = next_time
                heapq.heappush(q,(next_time,nx))

dijkstra(graph,time_list)

print(time_list[n])