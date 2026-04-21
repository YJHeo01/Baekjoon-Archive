import sys,heapq

input = sys.stdin.readline

n = int(input())

start = [True] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int,input().split())
    graph[parent].append((child,weight))
    graph[child].append((parent,weight))
    start[parent] = False

INF = int(1e9)

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nx, nd in graph[now]:
            if distance[nx] > dist + nd:
                distance[nx] = dist + nd
                heapq.heappush(q,(distance[nx],nx))
    ret_value = max(distance[1:])
    return ret_value

answer = 0
for i in range(1,n+1):
    if start[i] == True:
        distance = [INF] * (n+1)
        answer = max(dijkstra(graph,distance,i),answer)

print(answer)
