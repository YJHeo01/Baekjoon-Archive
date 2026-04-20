import sys,heapq

input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]


for _ in range(e):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))


house = [True] * (v+1)

m,x = map(int,input().split())

mcdonald = list(map(int,input().split()))

for i in mcdonald:
    house[i] = False

s,y = map(int,input().split())

starbucks = list(map(int,input().split()))

for i in starbucks:
    house[i] = False

mcdonald_distance = [x+1] * (v+1)
starbucks_distance = [y+1] * (v+1)

def dijkstra(graph,distance,start):
    q = []
    for i in start:
        distance[i] = 0
        heapq.heappush(q,(0,i))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, nd in graph[vx]:
            if distance[nx] > distance[vx] + nd:
                distance[nx] = distance[vx] + nd
                heapq.heappush(q,(distance[nx],nx))



INF = x+y+1
answer = INF

dijkstra(graph,mcdonald_distance,mcdonald)
dijkstra(graph,starbucks_distance,starbucks)

for i in range(1,v+1):
    if mcdonald_distance[i] > x or starbucks_distance[i] > y:
        continue
    answer = min(answer,mcdonald_distance[i]+starbucks_distance[i])

if answer >= INF:
    answer = -1

print(answer)