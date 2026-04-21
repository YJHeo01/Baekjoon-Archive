import heapq,sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    u,v,c = map(int,input().split())
    graph[v].append((u,c))

start = list(map(int,input().split()))

INF = float('inf')

def solution(start):
    q = []
    distance = [INF] * (n+1)
    for i in start:
        distance[i] = 0
        heapq.heappush(q,(0,i))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, cost in graph[vx]:
            if distance[nx] > dist + cost:
                distance[nx] = dist + cost
                heapq.heappush(q,(distance[nx],nx))
    max_distance = 0
    max_distance_city = 1
    for i in range(1,n+1):
        if distance[i] > max_distance:
            max_distance = distance[i]
            max_distance_city = i
    print(max_distance_city)
    print(max_distance)

solution(start)