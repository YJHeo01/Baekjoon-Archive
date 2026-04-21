import sys,heapq

input = sys.stdin.readline

v = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(v):
    tmp = list(map(int,input().split()))
    idx = tmp[0]
    i = 1
    while True:
        if tmp[i] == -1:
            break
        graph[idx].append((tmp[i],tmp[i+1]))
        i += 2

INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (v+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nx,l in graph[now]:
            if distance[nx] > dist + l:
                distance[nx] = dist + l
                heapq.heappush(q,(distance[nx],nx))
    return max(distance[1:])

answer = 0    
for i in range(1,v+1):
    answer = max(answer,dijkstra(i))

print(answer)