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
    
min_list.sort()

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


answer = 0

idx = 0

left, right = 0,0

for i in min_list:
    distance = [0] * (n+1)
    dijkstra(graph,distance,i)
    if distance[n] < i: continue
    left = i
    right = distance[n]
    while True:
        if idx == k: break
        if fish[idx] < left: idx += 1
        elif fish[idx] <= right:
            idx += 1
            answer += 1
        else:
            break


print(answer)