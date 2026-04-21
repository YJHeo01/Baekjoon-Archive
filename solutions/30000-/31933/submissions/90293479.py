import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

min_list = []
max_list = []

for _ in range(m):
    u,v,l,r = map(int,input().split())
    min_list.append(l)
    max_list.append(r)
    graph[u].append((v,l,r))
    graph[v].append((u,l,r))
    
k = int(input())

fish = sorted(list(map(int,input().split())))

tmp = []

INF = int(1e9)

def dijkstra(graph,distance,min_size):
    q = []
    distance[1] = INF
    heapq.heappush(q,(-INF,1))
    while q:
        dist, vx = heapq.heappop(q)
        dist *= -1
        if distance[vx] > dist: continue
        for nx,l,r in graph[vx]:
            if min_size < l or min_size > r: continue
            nd = min(r,dist)
            if nd > distance[nx]:
                distance[nx] = nd
                heapq.heappush(q,(-nd,nx))

for i in min_list:
    distance = [0] * (n+1)
    dijkstra(graph,distance,i)
    if distance[n] >= i:
        tmp.append((i,distance[n]))

def dijkstra_(graph,distance,max_size):
    q = []
    distance[1] = 0
    heapq.heappush(q,(0,1))
    while q:
        dist, vx = heapq.heappop(q)
        dist *= -1
        if distance[vx] > dist: continue
        for nx,l,r in graph[vx]:
            if max_size < l or max_size > r: continue
            nd = max(r,dist)
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

for i in max_list:
    break
    distance = [INF] * (n+1)
    dijkstra_(graph,distance,i)
    if distance[n] <= i:
        tmp.append((distance[n],i))
tmp.sort()

idx = 0

answer = 0

left, right = 0,0

for a,b in tmp:
    left = a
    right = max(right,b)
    while True:
        if idx == k: break
        if fish[idx] < left: idx += 1
        elif fish[idx] <= right:
            idx += 1
            answer += 1
        else:
            break

print(answer)